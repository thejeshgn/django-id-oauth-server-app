from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
urlpatterns = patterns('',

    url(r'^$',
        TemplateView.as_view(template_name='index.html'),
        name='index'),

    url(r'^accounts/',
        include('registration.backends.simple.urls')),

    url(r'^accounts/profile/',
        TemplateView.as_view(template_name='profile.html'),
        name='profile'),

    url(r'^login/',
        'django.contrib.auth.views.login',
        name='login'),
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)

