from django.conf.urls import patterns, url
from members import views

urlpatterns = patterns('',
	url(r'^$', views.member_login, name='login'),
	url(r'^logout/$', views.member_logout, name='logout'),
)