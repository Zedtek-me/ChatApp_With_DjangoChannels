from email import message
from email.mime import image
import re
from django.shortcuts import render, redirect
from .models import UserProfile, UploadedImage, Post
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import os

# Create your views here.


def index(request):
    # getting the users input at the index page
    if request.method== 'POST':
    #logging out the current user for a new user to log in, so that new old user session doesn't remain in the browser.
       logout(request)
       if request.POST.get('login'):
            name= request.POST.get('name')
            password= request.POST.get('pass')
            # validating that username and password are genuine...
            try:
                name= User.objects.get(username=name)
            except User.DoesNotExist:
                messages.error(request,'You are not registered yet!')
                return redirect('/chat/')
            if bool(name) != False:
                user= authenticate(request, username=name, password=password)
                if user:
                    try:
                        login(request, user)
                        return render(request, 'trends.html' ,{'name':name,})
                    except FileNotFoundError :
                        print(user.userprofile.image.save())
                messages.error(request, 'Username or Password is wrong!')
                return redirect('http://localhost:8000/chat/')
            
       elif request.POST.get('sign up'):
            return redirect('/signup/')
    else:
        if request.user.is_authenticated:
            print(request.session.get_expiry_date())
            return redirect('/trend/')
        else:
            message= messages.get_messages(request)
            return render(request, 'index.html', {'message' :message}) 

def signup(request):
    if request.method== 'POST':
        print(request.POST)
        # getting the sent data
        name= request.POST.get('name')
        surname= request.POST.get('surname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirm_pass= request.POST.get('pass_confirmation')
        # validating that username and email are unique, and tha passwords match
        if username in User.objects.all():
            messages.error(request, 'Username is already taken.')
            return redirect('/signup')
        # storing into the database if username is unique
        if password == confirm_pass:
            User.objects.create_user(first_name=name, last_name=surname, username=username, password=password, email=email)
            messages.success(request, 'You successfully signed up')
            return redirect('/chat')
        else: 
            messages.error(request, 'Your passwords didn\'t match!')
            return redirect('/signup')
    message= messages.get_messages(request)
    return render(request, 'signup.html', {"message" :message,})

def log_out(request):
    user=request.user
    print(user)
    logout(request)
    return redirect('http://localhost:8000')

# check whether it's an update or not (in profile)
@login_required(login_url='/chat')
def my_profile(request):
    user= request.user
    if request.method == 'POST':
        file= request.FILES.get('upload')
        posted_items= request.POST.get('post-widget')
        if file and posted_items:
            post= Post(owner=user, content=posted_items, image=file)
            post.save()
            messages.success(request, 'You Just Posted An Item Now!')
            return redirect('/profile/')
        elif posted_items and not file:
            post= Post(owner=user, content=posted_items)
            post.save()
            messages.success(request, 'You Just Posted An Item Without an Image Now!')
            return redirect('/profile/')
        else:
            post= Post(owner=user, content='', image=file)
            post.save()
            messages.success(request, 'You Just Posted an Image Now!')
            return redirect('/profile/')
    msg= messages.get_messages(request)
    post= user.post_set.all()
    return render(request, 'profile.html', {'user' :user,'message':msg, 'post':post})
        

# the base room
@login_required(login_url='/chat/')
def rooms(request):
    user= request.user
    return render(request, 'room.html', {'user':user})

# page after logging in
@login_required(login_url='/chat/')
def trends(request):
    user= request.user
    post= user.post_set.all()
    print(request.user)
    return render(request, 'trends.html', {'user':user,'post':post})

# for passwords forgotten
def forgot_pass(request):
    user= request.user
    return render(request, 'forgot_pass.html', {'user':user})


# Seeing user uploaded images
def uploaded(request):
    user= request.user
    myImages= user.uploadedimage_set.all()
    return render(request, 'user_uploads.html', {'uploaded': myImages,'user':user})


# settings
@login_required(login_url='/chat/')
def settings(request):
    user= request.user
    if request.method == 'POST':
        # get the new username and image
        username= request.POST.get('username')
        image= request.FILES.get('image')
        # updating
        if username:
            newName= User.objects.get(username=user)
            newName.username= username
            newName.save()
            # checking if the user uploaded a photo and whether the profile image of the user has not been manually deleted by an operator
            if image and newName.userprofile.image:
                # if the above condition is true, store a list of all profile photo in a variable 
                # and check the conditions that: the uploaded image is in the profile photo directory 
                # and it also has the name of the current userprofile image. If so, delete the current image from
                # the profile photo folder and remove it from being the profile image of the user. Then use the new one.This is to avoid duplicates, and to save space
                profile_photos= os.listdir('Profile_Media/profile_pics')
                if image in profile_photos and bool(str(newName.userprofile.image.url).split(image)):
                    # delete the present image associated with the user from the app storage and remove its association with profile.
                    print(image)
                    os.remove(newName.userprofile.image.path)
                    newName.userprofile.image.delete()
                    print('image removed from both folder and profile')
                    # now getting the profile of the user and adding the uploaded image to the profile.
                    Img_user= UserProfile.objects.get(user=newName)
                    Img_user.image=image
                    Img_user.save()
                    messages.info(request, 'Your profile has been updated. Reload now.')
                    return redirect('/profile/')
                Img_user= UserProfile.objects.get(user=newName)
                Img_user.image=image
                Img_user.save()
                messages.info(request, 'Your profile has been updated. You can reload.')
                return redirect('/profile/')
            return redirect('/profile/')
        else:
            profile_photos= os.listdir('Profile_Media/profile_pics')
            if image in profile_photos and bool(str(user.userprofile.image.url)):
                # delete the present image associated with the user from the app storage and remove its association.
                os.remove(user.userprofile.image.path)
                user.userprofile.image.delete()
                # now getting the profile of the user and adding the uploaded image to the profile.
                Img_user= UserProfile.objects.get(user=user)
                Img_user.image=image
                Img_user.save()
                messages.info(request, 'Your profile has been updated. Reload now.')
                return redirect('/profile/')
            print(user)
            Img_user= UserProfile.objects.get(user=user)
            Img_user.image=image
            Img_user.save()
            messages.info(request, 'Your profile has been updated. You can reload.')
            return redirect('/profile/')
    return render(request, 'settings.html', {'user':user})

# room view functions
@login_required(login_url='/chat/')
def science(request):
    user= request.user
    return render(request, 'forgot_pass.html', {'user':user})

@login_required(login_url='/chat/')
def general(request):
    user= request.user
    return render(request, 'forgot_pass.html', {'user':user})

@login_required(login_url='/chat/')
def personality(request):
    user= request.user
    return render(request, 'forgot_pass.html', {'user':user})

@login_required(login_url='/chat/')
def relationship(request):
    user= request.user
    return render(request, 'relationship.html', {'user':user})

@login_required(login_url='/chat/')
def philosophy(request):
    user= request.user
    return render(request, 'philosophy.html', {'user':user})