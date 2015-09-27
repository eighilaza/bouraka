from django.shortcuts import render
from django.models import Sponsor

def sponsors_list(request):
    sponsors = Sponsors.objects.all()
    template = 'sponsors/sponsors.html'
    context = { 'sponsors': sponsors }
    return render(request, template, context)
