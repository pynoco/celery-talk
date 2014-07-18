from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from store.views import HomePage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'celery_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomePage.as_view()),
    url(r'^admin/', include(admin.site.urls)),

)
