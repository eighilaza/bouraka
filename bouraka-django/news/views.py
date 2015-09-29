from django.shortcuts import render
from news.models import News

def index(request):
  news_list = News.objects.order_by('-publication_date')
  template = loader.get_template('news/news.html')
  context = { 'news_list': news_list }
  return render(request, template, context)
