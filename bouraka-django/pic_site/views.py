from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from news.models import New, Video, Image
from django.http import HttpResponseRedirect
def home(request):

	latest_news_list = New.objects.order_by('-publication_date')[:4]
	video_list = Video.objects.all()
	image_list = Image.objects.all()
	template = loader.get_template('pic_site/home.html')
	context = {
		'latest_news_list': latest_news_list,
		'video_list': video_list,
		'image_list': image_list,
		}

	return render(request, 'pic_site/home.html', context)

def gallery(request):
	return render(request, 'pic_site/gallery.html')
def sponsors(request):
	return render(request, 'pic_site/sponsors.html')
def history(request):
	return render(request, 'pic_site/history.html')
def team(request):
	return render(request, 'pic_site/team.html')
def shell(request):
	return render(request, 'pic_site/shell.html')
def educeco(request):
	return render(request, 'pic_site/educeco.html')
def michelin(request):
	return render(request, 'pic_site/michelin.html')
def results(request):
	return render(request, 'pic_site/results.html')
def futur(request):
	return render(request, 'pic_site/futur.html')
def envol(request):
	return render(request, 'pic_site/envol.html')
def epic(request):
	return render(request, 'pic_site/epic.html')
def orca(request):
	return render(request, 'pic_site/orca.html')
def elec(request):
	return render(request, 'pic_site/elec.html')
def roues(request):
	return render(request, 'pic_site/roues.html')
def moteur(request):
	return render(request, 'pic_site/moteur.html')
def simulateur(request):
	return render(request, 'pic_site/simulateur.html')
def accomplishments(request):
	return render(request, 'pic_site/accomplishments.html')
