"""
Main URLs configuration for project
"""
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',

    (r'^$', include("PROJECTDJPROJECT.website.urls")),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^favicon\.ico$', RedirectView.as_view(url='%sfavicon.ico' % settings.STATIC_URL)),
    (r'^favicon\.png',  RedirectView.as_view(url='%sfavicon.png' % settings.STATIC_URL)),
    (r'^apple-touch-icon\.png',  RedirectView.as_view(url='%sapple-touch-icon.png'  % settings.STATIC_URL)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )