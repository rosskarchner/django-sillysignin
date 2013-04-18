from django.conf.urls import patterns, url

from .views import SillyLogin, SillyLogout

urlpatterns = patterns('sillysignin.views',
                       url(r'^login/$', SillyLogin.as_view(),
                       name='login'),
                       url(r'^logout/$', SillyLogout.as_view(),
                       name='login'),
                       )
