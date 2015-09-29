from django.contrib import admin
from news.models import News, NewsImage

class InlineImage(admin.TabularInline):
  model = NewsImage

class NewsAdmin(admin.ModelAdmin):
  list_display = ('title', 'publication_date')
  inlines=[InlineImage]

admin.site.register(News, NewsAdmin)
