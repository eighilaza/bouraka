from django.shortcuts import render
from django.models import BureauMember

def sponsors_list(request):
    members = BureauMember.objects.all()
    template = 'bureau/members.html'
    context = { 'members': members }
    return render(request, template, context)
