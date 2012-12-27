from django.db import models

# Create your models here.

class cloth(models.Model):
    name = models.CharField(max_length = 50)
    style = models.CharField(max_length = 50)
    price = models.FloatField()
    