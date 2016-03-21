from django.contrib import admin
from results.models import Result, ResultImage 

class InlineImage(admin.TabularInline):
  model = ResultImage

class ResultAdmin(admin.ModelAdmin):
  list_display = ('title',)
  inlines=[InlineImage]

admin.site.register(Result, ResultAdmin)
