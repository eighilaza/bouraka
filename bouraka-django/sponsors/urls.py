from django.conf.urls import patterns, url
from sponsors import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
)
