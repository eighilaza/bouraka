from django.contrib import admin
from results.models import Result

class ResultAdmin(admin.ModelAdmin):
  list_display = ('year',)

admin.site.register(Result, ResultAdmin)
