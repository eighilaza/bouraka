from django.contrib import admin
from members.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'order')

admin.site.register(Member, MemberAdmin)
