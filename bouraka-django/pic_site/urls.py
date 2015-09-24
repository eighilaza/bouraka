from django.conf.urls import patterns, include, url
from django.contrib import admin
from pic_site import views
#from filebrowser.sites import site
#To serve media files
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^home/', 'pic_site.views.home'),
	#url(r'^gallery/', 'pic_site.views.gallery'),	
	url(r'^accomplishments/elec/', 'pic_site.views.elec'),
	url(r'^accomplishments/roues/', 'pic_site.views.roues'),
	url(r'^accomplishments/moteur/', 'pic_site.views.moteur'),
	url(r'^accomplishments/simulateur/', 'pic_site.views.simulateur'),
	url(r'^history/', 'pic_site.views.history'),
	url(r'^shell/', 'pic_site.views.shell'),
	url(r'^educeco/', 'pic_site.views.educeco'),
	url(r'^michelin/', 'pic_site.views.michelin'),
	url(r'^results/', 'pic_site.views.results'),
	url(r'^futur/', 'pic_site.views.futur'),
	url(r'^envol/', 'pic_site.views.envol'),
	url(r'^epic/', 'pic_site.views.epic'),
	url(r'^orca/', 'pic_site.views.orca'),
	url(r'^team/', 'pic_site.views.team'),
	url(r'^sponsors/', 'pic_site.views.sponsors'),	

	url(r'^actualites/', include('news.urls')),
	url(r'^members/', include('members.urls')),


    #url(r'^admin/filebrowser/', include(site.urls)),

    #url(r'^grappelli/', include('grappelli.urls')), 

    url(r'^admin/', include(admin.site.urls)),

    url(r'^photologue/', include('photologue.urls', namespace='photologue')),

	url(r'^$', 'pic_site.views.home'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
