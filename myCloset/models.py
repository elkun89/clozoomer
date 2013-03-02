from django.db import models
from django.contrib.auth.models import User

#===============================================================================
# Brand
#===============================================================================
class Brand(models.Model):
    name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.name  

#===============================================================================
# ApparelType
#===============================================================================
class ApparelType(models.Model):
    barcode = models.CharField(max_length = 100, unique = True)
    name = models.CharField(max_length = 50)
    price = models.FloatField()
    attribute = models.CharField(max_length = 50)
    pictureLink = models.CharField(max_length = 200)
    brand = models.ForeignKey(Brand)
    def __unicode__(self):
        return self.name+'('+self.brand.name+')'
    
#===============================================================================
# Apparel Instance
#===============================================================================
class ApparelInstance(models.Model):
    type = models.ForeignKey(ApparelType)
    timeOfCreation = models.DateTimeField(auto_now_add=True)
    locationOfPurchase = models.ForeignKey('Location')
    owner = models.ForeignKey(User, related_name='apparels')
    categories = models.ManyToManyField('Category', blank = True)
    def __unicode__(self):
        return self.name+'('+self.author.username+')'
    

#===============================================================================
# Cloth
#===============================================================================
class ClothType(ApparelType):
    pass
    
#===============================================================================
# Shoes
#===============================================================================
class ShoesType(ApparelType):
    pass

#===============================================================================
# Category
#===============================================================================
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
    
#===============================================================================
# UserProfile
#===============================================================================
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique = True)
    username = models.CharField(max_length = 200)
    firstname = models.CharField(max_length = 100, blank = True)
    lastname = models.CharField(max_length = 100, blank = True)
    email = models.EmailField(max_length = 200, blank = True)
    friends = models.ManyToManyField('UserProfile', blank = True)
    profielPictureLink = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.user.username


#===============================================================================
# Address of purchase
#===============================================================================
class Location(models.Model):
    address = models.CharField(max_length = 500);
    def __unicode__(self):
        return self.address;

    
