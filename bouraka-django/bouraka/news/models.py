#-*- coding: utf-8 -*-
from django.db import models

class New(models.Model):
	title = models.CharField(max_length = 100)
	text = models.TextField();
	publication_date = models.DateTimeField('published on:', auto_now_add = True)
	def __unicode__(self):
		return self.title

class Image(models.Model):
	new = models.ForeignKey(New)
	image = models.ImageField(upload_to = 'images/news')

class Video(models.Model):
	new = models.ForeignKey(New)
	video = models.CharField(max_length = 100)
