from django.contrib import admin
from slides.models import Slide, SlideImage 

class InlineImage(admin.TabularInline):
  model = SlideImage

class SlideAdmin(admin.ModelAdmin):
  list_display = ('title',)
  inlines=[InlineImage]

admin.site.register(Slide, SlideAdmin)
