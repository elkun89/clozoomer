# Create your views here
from django.contrib.auth.models import User, Permission
from myCloset.forms import *
from myCloset.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.core import serializers
from django.utils import simplejson
import json

def json_response(func):
    
    """
    
    @json_response
    
    A decorator thats takes a view response and turns it into json. If a callback is added
    through GET or POST the response is JSONP.
    
    Example usage:
    
    from django_decorators.decorators import json_response
    @json_response
    def any_view(request):
        return {'this will be': 'JSON'}
    
    Returns a JSON string.
    
    Now, if you need a JSONP response, just add a callback GET or POST variable. :)
    
    ---
    
    https://github.com/julian-amaya/django-decorators
    https://gist.github.com/871954
    https://gist.github.com/1568174
    
    """
    
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        callback = request.GET.get('callback', '')
        if isinstance(objects, HttpResponse):
            return objects
        # Even after using `functools.wraps`, I get:
        # Error: "'dict' object has no attribute 'status_code'".
#         if objects.status_code != 200:
#             return objects
        # It just seems like a good idea to check for a 200 status code... Oh well. :(
        try:
            data = simplejson.dumps(objects)
            if callback:
                # A jsonp response!
                data = callback + '(' + data + ');'
                return HttpResponse(data, 'text/javascript; charset=utf-8')
        except:
            data = simplejson.dumps(str(objects))
        return HttpResponse(data, 'application/json; charset=utf-8')
    return decorator

@login_required
def landing(request):
    return render(request, 'index.html')

def viewExample(request, categoryID, exampleID):
    template = loader.get_template('index.html')
    
    usrCategories = Category.objects.filter(author = request.user);
    usrApparel = Apparel.objects.filter(owner = request.user)
    
    context = Context({                                                 # Map the examples in HTML to the examples variable
                                                                        'usrCategories' : usrCategories,
                                                                        'usrApparel' : usrApparel,
                                                                        #'dependencies':dependencies,
    })
    return HttpResponse(template.render(context))

@json_response
def listApparelByJson(request):
    if request.is_ajax:
        #callback = request.GET.get('callback', '')
        userApparel = Apparel.objects.filter(owner = request.user)
        data = serializers.serialize('json', userApparel.all())
        #data = callback + '(' + data + ');'
        response = data;
    else:
        response = 'fail'
    return HttpResponse(response, content_type='application/json')

def randomTest(request):
    callback = request.GET.get('callback', '')
    req = {}
    req ['title'] = 'This is a constant result.'
    response = json.dumps(req)
    response = callback + '(' + response + ');'
    return HttpResponse(response, mimetype="application/json")

def register(request):
    newUser = User(is_staff = False, is_superuser = False)
    if request.method == 'POST':
        form = UserForm(request.POST)                                                   #make a user form filled with information from request.post
        if form.is_valid():                                                             #clean the data and store them in a newUser instance if the form is valid
            newUser.username = form.cleaned_data['username']
            newUser.first_name = form.cleaned_data['first_name']
            newUser.last_name = form.cleaned_data['last_name']
            newUser.email = form.cleaned_data['email']
            password = form.cleaned_data['newPassword']
            newUser.set_password(password)                                              #set the password for the newUser
            newUser.save()
            return HttpResponseRedirect('/accounts/login')
    else:
        form = UserForm()
    return render(request, 'signUp.html',{
            'form': form
    })
