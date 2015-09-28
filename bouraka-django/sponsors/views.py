from django.shortcuts import render
from sponsors.models import Sponsor

def index(request):
    sponsors_list = Sponsors.objects.all()
    groups_list = []
    for sponsor in sponsors_list:
        if sponsor.group not in groups_list:
            groups.append(sponsor.group)
    template = 'sponsors/sponsors.html'
    context = { 'sponsorsi_list': sponsors_list, 'groups_list': groups_list }
    return render(request, template, context)
