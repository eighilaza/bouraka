from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from news.models import News
from slides.models import Slide
from django.http import HttpResponseRedirect

def home(request):
    latest_news_list = News.objects.order_by('-publication_date')[:4]
    try:
         slide = Slide.objects.get(title='home')
    except Slide.DoesNotExist:
        slide = None 
    template = loader.get_template('bouraka/home.html')
    context = {
            'latest_news_list': latest_news_list,
            'slide': slide,
    }
    return render(request, 'bouraka/home.html', context)

def gallery(request):
    return render(request, 'bouraka/gallery.html')
def sponsors(request):
    return render(request, 'bouraka/sponsors.html')
def history(request):
    return render(request, 'bouraka/history.html')
def team(request):
    return render(request, 'bouraka/team.html')
def shell(request):
    return render(request, 'bouraka/shell.html')
def educeco(request):
    return render(request, 'bouraka/educeco.html')
def michelin(request):
    return render(request, 'bouraka/michelin.html')
def results(request):
    return render(request, 'bouraka/results.html')
def futur(request):
    return render(request, 'bouraka/futur.html')
def envol(request):
    return render(request, 'bouraka/envol.html')
def epic(request):
    return render(request, 'bouraka/epic.html')
def orca(request):
    return render(request, 'bouraka/orca.html')
def elec(request):
    return render(request, 'bouraka/elec.html')
def roues(request):
    return render(request, 'bouraka/roues.html')
def moteur(request):
    return render(request, 'bouraka/moteur.html')
def simulateur(request):
    return render(request, 'bouraka/simulateur.html')
def accomplishments(request):
    return render(request, 'bouraka/accomplishments.html')
def contacts(request):
    return render(request, 'bouraka/contacts.html')
