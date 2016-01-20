from django.shortcuts import render
from slides.models import Slide

def index(request, slide_name):
  slide = Slide.objects.get(title=slide_name)
  template = 'slide/home.html'
  context = { 'slide': slide }
  return render(request, template, context)
