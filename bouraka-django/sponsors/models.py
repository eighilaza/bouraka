from django.db import models

class Sponsor(models.Model):
    name = models.CharField( max_length = 150, blank = True )
    group = models.CharField( max_length = 150, blank = True )
    website = models.URLField( max_length = 150, blank = True )
    description = models.TextField( blank = True )
    logo = models.ImageField( upload_to = 'sponsors' )
    order = models.IntegerField()
    def __str__(self):
        return self.name

