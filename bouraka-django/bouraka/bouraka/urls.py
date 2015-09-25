"""bouraka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from bouraka import views

urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^home/', 'bouraka.views.home'),
        url(r'^accomplishments/elec/', 'bouraka.views.elec'),
        url(r'^accomplishments/roues/', 'bouraka.views.roues'),
        url(r'^accomplishments/moteur/', 'bouraka.views.moteur'),
        url(r'^accomplishments/simulateur/', 'bouraka.views.simulateur'),
        url(r'^history/', 'bouraka.views.history'),
        url(r'^shell/', 'bouraka.views.shell'),
        url(r'^educeco/', 'bouraka.views.educeco'),
        url(r'^michelin/', 'bouraka.views.michelin'),
        url(r'^results/', 'bouraka.views.results'),
        url(r'^futur/', 'bouraka.views.futur'),
        url(r'^envol/', 'bouraka.views.envol'),
        url(r'^epic/', 'bouraka.views.epic'),
        url(r'^orca/', 'bouraka.views.orca'),
        url(r'^team/', 'bouraka.views.team'),
        url(r'^sponsors/', 'bouraka.views.sponsors'),
        
        url(r'^actualites/', include('news.urls')),
        url(r'^members/', include('members.urls')),
        
        url(r'^$', 'bouraka.views.home'),
]
