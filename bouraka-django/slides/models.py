from django.db import models

class Slide(models.Model):
  title = models.CharField(max_length = 150)

def __str__(self):
  return self.title

class SlideImage(models.Model):
  slide = models.ForeignKey(Slide)
  image = models.ImageField()
