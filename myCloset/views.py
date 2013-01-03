# Create your views here
from django.contrib.auth.models import User, Permission
from myCloset.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from myCloset.models import *
from myCloset.serializers import *

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def brandList(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BrandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

@login_required
def landing(request):
    return HttpResponse('the landing page')

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
