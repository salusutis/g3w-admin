from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import (
    ListView,
)
from formtools.wizard.views import SessionWizardView
from guardian.shortcuts import get_objects_for_user
from collections import OrderedDict
from .models import *
from .forms import *
from qdjango.models import *

class CduConfigList(ListView):

    template_name = 'cdu/config_list.html'

    def get_queryset(self):
        return get_objects_for_user(self.request.user,'cdu.view_configs', Configs).order_by('title')


class CduConfigWizardView(SessionWizardView):
    """
    Wizard forms for CDU configuration managment
    """
    template_name = 'cdu/config_wizard.html'
    form_list = [
        cduConfigInitForm,
        cduConfigCatastoLayerForm,
        cduCatastoLayerFieldsForm,
        cduAgainstLayerFieldsForm,
        cduAgainstLayerFieldsAliasForm
    ]
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'tmp_cdu_odt_file'))

    def get_form_kwargs(self, step=None):
        if step == '0':
            return {'request': self.request}
        elif step == '1':
            return {'project': self.get_cleaned_data_for_step('0')['project']}
        elif step == '2' or step == '3':
            toRet = {'catastoLayerFormData': self.get_cleaned_data_for_step('1')}
            if step == '3':
                toRet['catastoLayerFieldsFormData'] = self.get_cleaned_data_for_step('2')
            return toRet
        if step == '4':
            return {'againstLayerFieldFormData': self.get_cleaned_data_for_step('3'), 'catastoLayerFieldsFormData': self.get_cleaned_data_for_step('2')}
        else:
            return {}

    def get_form_initial(self, step):
        if 'slug' in self.kwargs:
            pass
        else:
            res = {}
            # case insert
            if step == '2':
                dataStep1 = self.get_cleaned_data_for_step('1')
                self.againstLayers = Layer.objects.filter(id__in=dataStep1['againstLayers'])
                for l in self.againstLayers:
                    res[unicode2ascii(l.name)] = l.name.capitalize().replace('_', ' ')
            elif step == '3':
                dataStep2 = self.get_cleaned_data_for_step('2')
                for f in dataStep2['plusFieldsCatasto']:
                    res['plusFieldsCatasto_{}'.format(f)] = f.capitalize().replace('_', ' ')
            elif step == '4':
                dataStep3 = self.get_cleaned_data_for_step('3')
                for k, v in dataStep3.items():
                    for f in v:
                        res[f] = f.capitalize().replace('_', ' ')
            return res
        return {}

    def get_context_data(self, form, **kwargs):
        context = super(CduConfigWizardView, self).get_context_data(form=form, **kwargs)

        # get data for older step
        context['data_step'] = OrderedDict()
        for step in range(0, int(context['wizard']['steps'].current)):
            try:
                stepContexData = getattr(self, '_getContextDataStep{}'.format(str(step)))()
            except:
                stepContexData = self.get_cleaned_data_for_step(str(step))
            context['data_step'][str(step)] = stepContexData

        return context

    def _getContextDataStep0(self):
        rawData = self.get_cleaned_data_for_step('0')
        return {
            'title': rawData['title'],
            'project': Project.objects.get(pk=rawData['project']),
            'odtfile': rawData['odtfile']
        }

    def _getContextDataStep1(self):
        rawData = self.get_cleaned_data_for_step('1')
        return {
            'catastoLayer': Layer.objects.get(pk=rawData['catastoLayer']),
            'againstLayers': Layer.objects.filter(pk__in=rawData['againstLayers']),
        }

    def _getContextDataStep2(self):
        rawData = self.get_cleaned_data_for_step('2')
        angainstLayerAlias = {key: value for key, value in rawData.items() if key not in ['foglio','particella','plusFieldsCatasto']}
        return {
            'foglio': rawData['foglio'],
            'particella': rawData['particella'],
            'plusFieldsCatasto': rawData['plusFieldsCatasto'],
            'angainstLayerAlias': angainstLayerAlias
        }

