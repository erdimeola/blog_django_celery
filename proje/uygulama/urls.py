from django.conf.urls import patterns, url

from uygulama import views

urlpatterns = patterns('uygulama.views',
    url(r'', views.index, name="index"),
)
