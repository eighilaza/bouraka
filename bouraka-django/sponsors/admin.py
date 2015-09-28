from django.contrib import admin
from sponsors.models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name')

admin.site.register(Sponsor)
#,MemberAdmin)
