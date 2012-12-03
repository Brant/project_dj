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
    
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
    (r'^favicon\.png', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.png'}),
    (r'^apple-touch-icon\.png', 'django.views.generic.simple.redirect_to', {'url': '/static/apple-touch-icon.png'}),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )