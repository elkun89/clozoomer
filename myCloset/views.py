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
                                                                        #'allPosts' : userPosts
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
            newProfile.user = newUser
            newProfile.username = newUser.username
            newProfile.first_name = newUser.first_name
            newProfile.last_name = newUser.last_name
            newProfile.email = newUser.email
            newProfile.gender = form.cleaned_data['gender']
            newProfile.profilePictureLink = "/media/users/defaultProfile.jpg"
            newProfile.save()
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

##
# function to get the friends of a certain user
# @param request: the http request sent by the user

@api_view(['GET'])
def getFriends(request):
    uprofile = UserProfile.objects.get(user = request.user)
    ufriends = UserProfile.objects.filter(id__in = uprofile.friends.all())
    serializer = UserProfileSerializer(ufriends)
    #assert False, serializer.data
    
    return Response(serializer.data)

##
# functions to get and to edit profiles
# @param request: the http request sent by the user

@api_view(['GET'])
def getProfile(request):
    uprofile = UserProfile.objects.get(user = request.user)
    serializer = UserProfileSerializer(uprofile)
    return Response(serializer.data)
##
# function to edit profile
# @param request: the http request sent by the user

@login_required
def editProfile(request):
    oldProfile = UserProfile.objects.get(user = request.user)
    if request.method == 'POST':                                    #process the information if the request is post
        form = ProfileForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            newProfile = form.save(commit = False)
            newProfile.user = request.user
            newProfile.username = request.user.username
            new_picture_link = form.cleaned_data['profilePictureLink']
            if not new_picture_link:
                newProfile.profilePictureLink = oldProfile.profilePictureLink
            oldProfile.delete()
            newProfile.save()
            return HttpResponseRedirect('/')
    else:
        form = ProfileForm(request.user, instance = oldProfile, initial = {})
    return render(request, 'formTemplate.html', {
            'form': form
    })


##
# function to display posts to friends
# @param request: the http request sent by the user

@api_view(['GET'])
def showPosts(request):
    uprofile = UserProfile.objects.get(user = request.user)
    ufriends = UserProfile.objects.filter(id__in = uprofile.friends.all())
    user_posts = list()
    user_profile_list = list(ufriends)
    user_profile_list.append(uprofile)

    if not user_profile_list:
        return Response('');
    
    for user_profile in user_profile_list:
        posts = Post.objects.filter(author = user_profile.user)
        for post in posts:
            user_posts.append(post);
    serializer = PostSerializer(user_posts);
    return Response(serializer.data);

##
# function to create posts
# @param request: the http request sent by the user

@login_required
def createPost(request):
    if request.method == 'POST':                                    #process the information if the request is post
        form = PostForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            newPost = form.save(commit = False)
            newPost.author = request.user
            newPost.save()
        return HttpResponseRedirect('/#show_livefeed')
    else:
        form = PostForm(request.user)
        url = '/newPost/'
        return render(request, 'new_form_template.html', {
            'form': form,
            'url' : url
        })
        
##
# function to add apparel instances
# @param request: the http request sent by the user

@login_required
def add_apparel_instance(request):
    if request.method == 'POST':                                    
        form = InstanceForm(request.POST)
        if form.is_valid():
            newInstance = ApparelInstance()
            newInstance.category = form.cleaned_data['categories']
            newInstance.owner = request.user
            cleaned_barcode = form.cleaned_data['barcode']
            newInstance.type = ApparelType.objects.get(barcode = cleaned_barcode)
            newInstance.save()
            return HttpResponseRedirect('/#apparel_nojson_request')
        else:
            return HttpResponse("Form data not valid!")
    else:
        form = InstanceForm()
        url = '/addApparelInstance/'
        return render(request, 'new_form_template.html', {
            'form': form,
            'url' : url
        })
        
##
# function to add apparel instances
# @param request: the http request sent by the user

@login_required
def add_friend_request(request):
    if request.method == 'POST':                                    
        form = FriendAddForm(request.user, request.POST)
        if form.is_valid():
            new_request = FriendRequest()
            new_request.requested_user = form.cleaned_data['requested_user']
            new_request.message = form.cleaned_data['message']
            new_request.requester = UserProfile.objects.get(user = request.user)
            new_request.save()
            return HttpResponseRedirect('/#request_friend_success')
        else:
            return HttpResponse("Form data not valid!")
    else:
        form = FriendAddForm(request.user)
        url = '/requestFriend/'
        return render(request, 'new_form_template.html', {
            'form': form,
            'url' : url
        })



##
# function to display own posts in closet
# @param request: the http request sent by the user

@login_required
@api_view(['GET'])
def displayCloset(request):
    userPosts = list()

    posts = Post.objects.filter(author = request.user)
    if len(posts) == 0:
        return Response('');
    else:
        for post in posts:
            userPosts.append(post);
            serializer = PostSerializer(userPosts);
            
        return Response(serializer.data);

##
# function to delete apparel instances
# @param request: the http request from the user
# @param idNum: the id of the apparel instance to be deleted
 
def delete_apparel_instance(request, idNum):
    try:
        apparel_to_delete = ApparelInstance.objects.get(id = idNum)
        apparel_to_delete.delete()
        return HttpResponseRedirect("/#apparel_nojson_request")
    except:
        return HttpResponse("Deletion failed: object not found!")
    
##
# function to delete posts
# @param request: http request from the user
# @param idNum: the id of the post to be deleted

@login_required
def delete_post(request, idNum):
    try:
        post_to_delete = Post.objects.get(id = idNum)
        if request.user == post_to_delete.author: 
            post_to_delete.delete()
            return HttpResponseRedirect("/#show_livefeed")
        else:
            return HttpResponse("Deletion failed: you don't own this post!")
    except:
        return HttpResponse("Deletion failed: object not found!")
    

##
# function to list the current friend requests to the user

@login_required
def show_friend_request(request):
    user_profile = UserProfile.objects.get(user = request.user)
    friend_requests = FriendRequest.objects.filter(requested_user = user_profile, processed = False)
    form = FriendConfirmForm()
    url = '/processFriendRequest/'
    #form.fields['requester'].widget = forms.HiddenInput()
    return render(request, 'show_friend_request_form.html', {
        'form': form,
        'url' : url,
        'friend_requests' : friend_requests
    })
    
def process_friend_request(request):
    user_profile = UserProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = FriendConfirmForm(request.POST)
        if form.is_valid():
            this_requester = form.cleaned_data['requester']
            responded_requests = FriendRequest.objects.filter(requester = this_requester, requested_user = user_profile)
            if form.cleaned_data['response'] == True:
                this_requester.friends.add(user_profile)
                user_profile.friends.add(this_requester)
            for each_responded_request in responded_requests:
                each_responded_request.processed = True
                each_responded_request.save()
            return HttpResponseRedirect("/#friends_request")
    return HttpResponse("Error in data!")
                





