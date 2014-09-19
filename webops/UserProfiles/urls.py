from django.conf.urls import patterns, include, url
from UserProfiles import views
from django.contrib.auth.models import User
from UserProfiles.models import Student

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^register/$', views.user_register, name = 'user_register'),
	url(r'^login/$', views.user_login, name = 'user_login'),
	url(r'^logout/$', views.user_logout, name = 'user_logout'),
	url(r'^(?P<student_id>\d+)/$', views.user_detail, name = 'user_detail'),
	url(r'^(?P<student_id>\d+)/edit/$', views.user_edit, name = 'user_edit'),
	#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),	
)
