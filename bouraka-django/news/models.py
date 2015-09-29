from django.db import models

class News(models.Model):
  title = models.CharField(max_length = 150)
  text = models.TextField();
  publication_date = models.DateTimeField('published on:', auto_now_add = True)
  def __str__(self):
    return self.title

class NewsImage(models.Model):
  news = models.ForeignKey(News)
  image = models.ImageField()
