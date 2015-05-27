from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CSBCD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'dashboards.views.home', name = 'home'),
    url(r'^signup', 'signups.views.join', name = 'signup'),
    url(r'^chart', 'charts.views.chart', name = 'chart'),
    url(r'^table', 'tables.views.table', name = 'table'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax/', 'dashboards.views.ajax'),
    url(r'^temperature_json/', 'dashboards.views.ajax'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root = settings.MEDIA_ROOT)
