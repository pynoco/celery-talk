from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings

from store.views import HomePage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'celery_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomePage.as_view()),
    url(r'^store/', include('store.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
