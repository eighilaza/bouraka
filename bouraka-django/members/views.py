from django.shortcuts import render
from members.models import Member

def index(request):
    members_list = Member.objects.order_by('order')
    teams_list = []
    for member in members_list:
        if member.team not in teams_list:
            teams_list.append(member.team)
    teams_list.sort()
    template = 'members/members.html'
    context = { 'members_list': members_list, 'teams_list': teams_list }
    return render(request, template, context)
