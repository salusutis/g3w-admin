from django.forms import ModelForm


class G3WRequestFormMixin(object):
    """ Form Mixin to get Request object from instance """

    def __init__(self, *args, **kwargs):

        #get request object from kwargs
        if 'request' in kwargs:
            self.request = kwargs['request']
            del(kwargs['request'])

        #for not model form:
        if not isinstance(self,ModelForm):
            del(kwargs['instance'])
        super(G3WRequestFormMixin, self).__init__(*args, **kwargs)

class G3WFormMixin(object):
    """ Form mixin for crispy form layout element """

    def checkEmptyInitialsData(self,*fields):

        if not hasattr(self,'initial') or len(self.initial.items()) == 0:
            return 'collapsed-box'
        collapsed = True

        for field in fields:
            if field in self.initial and (not self.initial[field] or self.initial[field] != ''):
                collapsed = False

        return 'collapsed-box' if collapsed else ''

    def checkFieldsVisible(self,*fields):

        visible = True

        if len(set(fields).intersection(set(self.fields))) > 0:
            visible = False

        return 'hidden' if visible else ''