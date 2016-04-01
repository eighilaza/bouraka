from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Result(models.Model):
  year = models.PositiveIntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2200)])
  description = models.CharField(max_length = 500)
  def __str__(self):
    return str(self.year)
