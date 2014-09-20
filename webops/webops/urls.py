from django.conf.urls import patterns, include, url
from UserProfiles.models import Student
from sessions.models import SessionDetails
from django.contrib import admin
from webops import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
	url(r'^UserProfiles/', include('UserProfiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sessions/', include('sessions.urls')),
    url(r'^index', 'index'),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    #url(r'^accounts/login/$', 'login'),
	#url(r'^accounts/logout/$', 'logout'),
	#url(r'^accounts/register/$', 'register'),

)
