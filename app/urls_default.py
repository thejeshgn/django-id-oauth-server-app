from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import UserAPI

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^accounts/profile/',TemplateView.as_view(template_name='profile.html'),
        name='profile'),
    url(r'^login/','django.contrib.auth.views.login',name='login'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/user$', UserAPI.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
