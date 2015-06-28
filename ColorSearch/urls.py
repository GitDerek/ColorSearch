from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'ColorSearch.views.home', name='home'),
                       url(r'^info/', 'ColorSearch.views.info', name='info'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
