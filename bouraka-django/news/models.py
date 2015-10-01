from django.db import models
import datetime

class News(models.Model):
  title = models.CharField(max_length = 150)
  text = models.TextField();
  publication_date = models.DateTimeField('published on:', default=datetime.datetime.now)
  def __str__(self):
    return self.title

class NewsImage(models.Model):
  news = models.ForeignKey(News)
  image = models.ImageField()
