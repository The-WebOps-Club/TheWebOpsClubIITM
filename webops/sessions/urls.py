from django.conf.urls import patterns, include, url
from sessions import views
from django.contrib.auth.models import User
from sessions.models import SessionDetails

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^create/$', views.create_new, name = 'create_new'),
	url(r'^(?P<SessionDetails_id>\d+)/$', views.detail, name = 'detail'),
	url(r'^(?P<SessionDetails_id>\d+)/join/$', views.join_session, name = 'join_session'),
	url(r'^(?P<SessionDetails_id>\d+)/details/$', views.detail, name = 'session_details')
	)

