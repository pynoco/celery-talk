from django.conf.urls import *

from store.views import sync_upload, async_upload

urlpatterns = patterns('',
    url(r'^sync_upload/$', sync_upload, name='sync_upload'),
    url(r'^async_upload/$', async_upload, name='async_upload'),

)
