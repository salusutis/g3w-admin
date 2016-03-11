from django.conf.urls import url
from .views import uploadform, fileupload, ExampleFormView, ExampleAjaxFormView
from django.contrib.auth.decorators import login_required
from .views import *

from django.views.static import serve
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


urlpatterns = [
    url(r'^$', uploadform, name='home'),
    url(r'^file-upload/$', fileupload),

    #group urls
    url(r'^groups/$', login_required(GroupListView.as_view()), name='group-list'),
    url(r'^groups/add/$', login_required(GroupCreateView.as_view()), name='group-add'),
    url(r'^groups/update/(?P<slug>[-_\w\d]+)/$',login_required(GroupUpdateView.as_view()), name='group-update'),
    url(r'^groups/delete/(?P<slug>[-_\w\d]+)/$',login_required(GroupDeleteView.as_view()), name='group-delete'),
    url(r'^groups/(?P<slug>[-_\w\d]+)/$',login_required(GroupDetailView.as_view()), name='group-detail'),

    #project urls
    url(r'^groups/(?P<group_slug>[-_\w\d]+)/projects/$', login_required(ProjectListView.as_view()), name='project-list'),

    #exmaple file form ajax
    url(r'^exampleform/$', ExampleFormView.as_view()),
    url(r'^exampleajaxform/$', ExampleAjaxFormView.as_view()),

    #url(r'^{}(?P<path>.*)$'.format(settings.MEDIA_URL[1:] + 'logo_img/'), protected_serve, {'document_root': settings.MEDIA_ROOT+ 'logo_img/'}),

]