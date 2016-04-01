from django.shortcuts import render
from results.models import Result

def index(request):
    results_list = Result.objects.order_by('-year')
    template = 'results/results.html'
    context = { 'results_list': results_list }
    return render(request, template, context)
