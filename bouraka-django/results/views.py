from django.shortcuts import render
from results.models import Result

def index(request, result_name):
  result = Result.objects.get(title=result_name)
  template = 'result/home.html'
  context = { 'result': result }
  return render(request, template, context)
