from django.contrib import admin
from members.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name')

admin.site.register(Member)
#,MemberAdmin)
