from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Permission

class Brand(models.Model):
    name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.name  

class Apparel(models.Model):
    barcode = models.CharField(max_length = 100)
    name = models.CharField(max_length = 50)
    price = models.FloatField()
    attribute = models.CharField(max_length = 50)
    pictureLink = models.CharField(max_length = 200)
    locationOfPurchase = models.CharField(max_length = 200)
    brand = models.ForeignKey(Brand)
    owner = models.ForeignKey(User, related_name='apparels')
    categories = models.ManyToManyField('Category', blank = True)
    def __unicode__(self):
        return self.name+'('+self.author.username+')'
    

class Cloth(Apparel):
    pass
    
class Shoes(Apparel):
    pass

class Category(models.Model):
    author = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    description = models.TextField()
    PERMISSIONS = (
        ('S', 'Shared'),
        ('P', 'Private'),
    )
    permission = models.CharField(max_length = 2, choices = PERMISSIONS)
    def __unicode__(self):
        return self.name+'('+self.author.username+')'
    
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    profielPictureLink = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.user.username
    

    
