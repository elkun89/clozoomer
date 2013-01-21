from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
    
class AllowJSONPCallback(object):
    """This decorator function wraps a normal view function                                                                                      
    so that it can be read through a jsonp callback.                                                                                             
                                                                                                                                                 
    Usage:                                                                                                                                       
                                                                                                                                                 
    @AllowJSONPCallback                                                                                                                          
    def my_view_function(request):                                                                                                               
        return HttpResponse('this should be viewable through jsonp')                                                                             
                                                                                                                                                 
    It looks for a GET parameter called "callback", and if one exists,                                                                           
    wraps the payload in a javascript function named per the value of callback.                                                                  
                                                                                                                                                 
    Using AllowJSONPCallback implies that the user must be logged in                                                                             
    (and applies automatically the login_required decorator).                                                                                    
    If callback is passed and the user is logged out, "notLoggedIn" is                                                                           
    returned instead of a normal redirect, which would be hard to interpret                                                                      
    through jsonp.                                                                                                                               
                                                                                                                                                 
    If the input does not appear to be json, wrap the input in quotes                                                                            
    so as not to throw a javascript error upon receipt of the response."""
    def __init__(self, f):
        self.f = login_required(f)

    def __call__(self, *args, **kwargs):
        request = args[0]
        callback = request.GET.get('callback')
        # if callback parameter is present,                                                                                                      
        # this is going to be a jsonp callback.                                                                                                  
        if callback:
            if request.user.is_authenticated():
                try:
                    response = self.f(*args, **kwargs)
                except:
                    response = HttpResponse('error', status=500)
                if response.status_code / 100 != 2:
                    response.content = 'error'
            else:
                response = HttpResponse('notLoggedIn')
            if response.content[0] not in ['"', '[', '{'] \
                    or response.content[-1] not in ['"', ']', '}']:
                response.content = '"%s"' % response.content
            response.content = "%s(%s)" % (callback, response.content)
            response['Content-Type'] = 'application/javascript'
        else:
            response = self.f(*args, **kwargs)
        return response
    

    
