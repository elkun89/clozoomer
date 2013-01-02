# Create your views here
from django.contrib.auth.models import User, Permission
from myCloset.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
