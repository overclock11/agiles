from django.db import models

# Create your models here.
class Mascota(models.Model):
    identification = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateField()