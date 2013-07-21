from django.db import models
from django.contrib.auth.models import User
from closetapp.settings import MEDIA_ROOT
import os

def get_upload_path(instance, filename):
    return os.path.join(
      "user_%s" % instance.user.username, filename)

#===============================================================================
# Brand
#===============================================================================
class Brand(models.Model):
    name = models.CharField(max_length = 100)
    def __unicode__(self):
        return u"%s" % (self.name)  

#===============================================================================
# ApparelType
#===============================================================================
class ApparelType(models.Model):
    barcode = models.CharField(max_length = 100, unique = True)
    name = models.CharField(max_length = 50)
    price = models.FloatField()
    attribute = models.CharField(max_length = 50)
    pictureLink = models.ImageField(upload_to = 'apparel_types', blank = True)
    brand = models.ForeignKey(Brand)
    def __unicode__(self):
        return self.name+'('+self.brand.name+')'
    
#===========================
# Apparel Instance
#===============================================================================
class ApparelInstance(models.Model):
    type = models.ForeignKey(ApparelType)
    timeOfCreation = models.DateTimeField(auto_now_add=True)
    #locationOfPurchase = models.ForeignKey('Location')
    owner = models.ForeignKey(User, related_name='apparels')
    categories = models.ManyToManyField('Category', blank = True)
    is_shared = models.BooleanField()
    def __unicode__(self):
        return self.type.name+'('+self.owner.username+')'
    

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
    username = models.CharField(max_length = 200, unique = True)
    first_name = models.CharField(max_length = 100, blank = True)
    last_name = models.CharField(max_length = 100, blank = True)
    email = models.EmailField(max_length = 200)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length = 2, choices = GENDER)
    friends = models.ManyToManyField('UserProfile', blank = True)
    profilePictureLink = models.ImageField(upload_to = get_upload_path, blank = True)
    posts = models.ManyToManyField('Post', blank = True)
    
    
    
    def __unicode__(self):
        return u"%s" % (self.user.username)
    
    

#===============================================================================
# Address of purchase
#===============================================================================
class Location(models.Model):
    address = models.CharField(max_length = 500);
    def __unicode__(self):
        return u"%s" % (self.address);


##
# Model to hold the information of posts created by the user
# @param author: the author of the post 
# @param content: The post's content
# @param keywords: The keywords or tags associated with this post
# @param mainPicture: The picture which the user wishes to post
# @param userPictures: The pictures of the current user

class Post(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length = 500)
    keywords = models.ManyToManyField('Keyword', blank = True)
    mainPicture = models.ImageField(upload_to = 'users', blank = True)
    userPictures = models.ImageField(upload_to = 'users', blank = True)
    def __unicode__ (self):
        return self.content+'('+self.author.username+')'

##
# Model to hold requests sent by users to make friends
# @param message: the message from the user making the request
# @param requester: the user making the request
# @param response: boolean value indicating whether the request is granted
# @param processed: boolean value indicating whether the request is processed
 
class FriendRequest(models.Model):
    message = models.CharField(max_length = 500)
    timeOfCreation = models.DateTimeField(auto_now_add=True, editable = False)
    requester = models.ForeignKey(UserProfile)
    requested_user = models.ForeignKey(UserProfile, related_name = 'user_requested')
    response = models.BooleanField(blank = True)
    processed = models.BooleanField(default = False)
    
    def __unicode__ (self):
        return 'Request from ' + self.requester.username + ' to ' + self.requested_user.username

##
# Model to hold keywords used by posts for searching according to keywords
# @param word: The word a keyword instance contains

class Keyword(models.Model):
    word = models.CharField(max_length = 20, unique = True)

    def __unicode__ (self):
        return '(' + self.word + ')'











    
