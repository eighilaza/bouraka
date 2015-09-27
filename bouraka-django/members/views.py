from django.shortcuts import render
from django.models import Member

def members_list(request):
    members = Member.objects.all()
    template = 'members/members.html'
    context = { 'members': members }
    return render(request, template, context)
