from django.shortcuts import render
from slides.models import Slide

def index(request, salide_name):
  slide = Slide.objects.get(title=slide_name)
  template = 'slide/news.html'
  context = { 'news_list': news_list }
  return render(request, template, context)
