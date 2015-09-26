from django.db import models

# Create your models here.
class BureauMemeber(models.Model):
    name = models.CharField( max_length = 150, blank = True )
    title = models.CharField( max_length = 150, blank = True )
    team = models.CharField( max_length = 150, blank = True )
    departement = models.IntegerField( blank = True  )
    year = models.IntegerField( blank = True )
    description = models.TextField( blank = True )
    photo = models.ImageField( upload_to = 'members' )
    def __str__(self):
        return self.name
