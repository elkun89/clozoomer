# Create your views here
from django.contrib.auth.models import User, Permission
from myCloset.forms import *
from myCloset.models import *
from myCloset.restapi.serializers import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import sys
import traceback

#===============================================================================
# function used to debug
#===============================================================================
def console_debug(f):
    def x(*args, **kw):
        try:
            ret = f(*args, **kw)
        except Exception, e:
            print >> sys.stderr, "ERROR:", str(e)
            exc_type, exc_value, tb = sys.exc_info()
            message = "Type: %s\nValue: %s\nTraceback:\n\n%s" % (exc_type, exc_value, "\n".join(traceback.format_tb(tb)))
            print >> sys.stderr, message
            raise
        else:
            return ret
    return x

#===============================================================================
# landing function for the index page
# @param request: the http request sent by user
# @return: the template with rendered context 
#===============================================================================
@login_required
def landing(request):
    template = loader.get_template('index.html')
    
    usrCategories = Category.objects.filter(author=request.user);
    usrApparel = ApparelInstance.objects.filter(owner=request.user);
    apparelType = ApparelType.objects.all();
    apparelLocation = Location.objects.all();
    thisUser = request.user;
    thisProfile = UserProfile.objects.get(user = request.user);
    
    context = Context({  # Map the examples in HTML to the examples variable
                                                                        'usrCategories' : usrCategories,
                                                                        'usrApparel' : usrApparel,
                                                                        'apparelType' : apparelType,
                                                                        'apparelLocation' : apparelLocation,
                                                                        'thisUser' : thisUser,
                                                                        'thisProfile' : thisProfile,
    })
    return HttpResponse(template.render(context))

#===============================================================================
# function to give information of the user's apparel
# @param  request: the ajax GET request 
# @return: json data of apparel information 
#===============================================================================
@login_required
@console_debug
@api_view(['GET'])
def listApparelByJson(request):
    if request.method == 'GET':
        usrApparel = ApparelInstance.objects.filter(owner = request.user)
        instanceSerializer = ApparelInstanceSerializer(usrApparel)
        return Response(instanceSerializer.data)
    
#===============================================================================
# function to list all user's categories by json
# @param request: the ajax request 
# @return: json data containing category information  
#===============================================================================
@login_required
@api_view(['GET'])
def listCategoryByJson(request):
    if request.method == 'GET':
        usrCategories = Category.objects.filter(author = request.user);
        serializer = CategorySerializer(usrCategories)
        return Response(serializer.data)

#===============================================================================
# function to request the user's information
# @param  request: the ajax request sent by the user
# @return : serialized user data in json format  
#===============================================================================
@login_required
@api_view(['GET'])
def requestUserProfile(request):
    if request.method == 'GET':
        users = User.objects.filter(username = request.user.username);
        serializer = UserSerializer(users)
        return Response(serializer.data)

#===============================================================================
# function to do rando jsonp tests
# @param request: the http request
# @return: the response containing json data wrapped in jsonp format
#===============================================================================
@login_required
def randomTest(request):
    callback = request.GET.get('callback', '')
    req = {}
    req ['title'] = 'This is a constant result.'
    response = json.dumps(req)
    response = callback + '(' + response + ');'
    return HttpResponse(response, mimetype="application/json")

#===============================================================================
# function to register users
# @param request: the http request
# @return : render form for the user to sign up or upon success redirect to login. 
#===============================================================================
def register(request):
    newUser = User(is_staff=False, is_superuser=False)
    if request.method == 'POST':
        form = UserForm(request.POST)  # make a user form filled with information from request.post
        if form.is_valid():  # clean the data and store them in a newUser instance if the form is valid
            newUser.username = form.cleaned_data['username']
            newUser.first_name = form.cleaned_data['first_name']
            newUser.last_name = form.cleaned_data['last_name']
            newUser.email = form.cleaned_data['email']
            password = form.cleaned_data['newPassword']
            newUser.set_password(password)  # set the password for the newUser
            newUser.save()
            
            #copy the information to profile
            newProfile = UserProfile()
            newProfile.username = newUser.username
            newProfile.firstname = newUser.first_name
            newProfile.lastname = newUser.last_name
            newProfile.email = newUser.email
            return HttpResponseRedirect('/accounts/login')
    else:
        form = UserForm()
    return render(request, 'signUp.html', {
            'form': form
    })
    
#===============================================================================
# function to get the type of the specified apparel
# @param request: the http request sent by the user
# @param idNum: the id of the apparel
#===============================================================================
@api_view(['GET'])
def getApparelType(request, idNum):
    if request.method == 'GET':
        apparelType = ApparelType.objects.get(id = idNum)
        serializer = ApparelTypeSerializer(apparelType)
        return Response(serializer.data)
    
#===============================================================================
# function to get apparel without using json
# @param request: the http request sent by the user
# @param idNum: the id of the apparel
#===============================================================================
@login_required
def listApparel(request):
    template = loader.get_template('index.html')
    
    usrCategories = Category.objects.filter(author=request.user);
    usrApparel = ApparelInstance.objects.filter(owner=request.user);
    apparelType = ApparelType.objects.all();
    apparelLocation = Location.objects.all();
    thisUser = request.user;
    
    context = Context({  # Map the examples in HTML to the examples variable
                                                                        'usrCategories' : usrCategories,
                                                                        'usrApparel' : usrApparel,
                                                                        'apparelType' : apparelType,
                                                                        'apparelLocation' : apparelLocation,
                                                                        'thisUser' : thisUser,
    })
    return HttpResponse(template.render(context))

#===============================================================================
# function to get the friends of a certain user
# @param request: the http request sent by the user
#===============================================================================
@api_view(['GET'])
def getFriends(request):
    uprofile = UserProfile.objects.get(user = request.user)
    ufriends = UserProfile.objects.filter(id__in = uprofile.friends.all())
    serializer = UserProfileSerializer(ufriends)
    return Response(serializer.data)

#===============================================================================
# function to get the friends of a certain user
# @param request: the http request sent by the user
#===============================================================================
@api_view(['GET'])
def getProfile(request):
    uprofile = UserProfile.objects.get(user = request.user)
    serializer = UserProfileSerializer(uprofile)
    return Response(serializer.data)









