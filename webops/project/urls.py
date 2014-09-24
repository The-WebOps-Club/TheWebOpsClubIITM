from django.conf.urls import patterns, include, url
from project import views
from django.contrib.auth.models import User
from project.models import ProjectDetails

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^create/$', views.create_new, name = 'create_new'),
	url(r'^(?P<ProjectDetails_id>\d+)/$', views.detail, name = 'detail'),
	url(r'^(?P<ProjectDetails_id>\d+)/join/$', views.join_project, name = 'join_project'),
	url(r'^(?P<ProjectDetails_id>\d+)/details/$', views.detail, name = 'project_details')
	)

