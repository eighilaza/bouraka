from django.contrib import admin
from members.models import Member

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(Slide, SlideAdmin)
