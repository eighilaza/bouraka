from django.db import models

class Result(models.Model):
  title = models.CharField(max_length = 150)
  def __str__(self):
    return self.title

class ResultImage(models.Model):
  result = models.ForeignKey(Result)
  image = models.ImageField()
