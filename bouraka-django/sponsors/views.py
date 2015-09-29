from django.shortcuts import render
from sponsors.models import Sponsor

def index(request):
    sponsors_list = Sponsor.objects.order_by('order')
    groups_list = []
    for sponsor in sponsors_list:
        if sponsor.group not in groups_list:
            groups_list.append(sponsor.group)
    groups_list.sort()
    template = 'sponsors/sponsors.html'
    context = { 'sponsors_list': sponsors_list, 'groups_list': groups_list }
    return render(request, template, context)
