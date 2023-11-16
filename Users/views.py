from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Credentials, Users
from django.contrib.auth.hashers import make_password, check_password

def login(request):
    if request.method == 'POST':
        print("Loggeg in")
    elif request.method == 'GET':
        return render(request, 'Users/login.html')

def signup(request):
    if request.method == 'POST':
        try:
            credential = Credentials(email = request.POST['email'], password = make_password(request.POST['password']))
            credential.save()
        except:
            context = {'error' : True, 'message':"Invalid Credentials, try again."}
            return render(request, 'Users/signup.html', context)

        try:
            user = Users(first_name = request.POST['firstName'], last_name = request.POST['lastName'], user_credential = credential)
            user.save()
        except:
            context = {'error' : True, 'message':"Invalid User Information, try again."}
            return render(request, 'Users/signup.html', context)


        context = {'error' : False, 'message':"User Created Successfully."}
        return render(request, 'Users/signup.html', context)
    elif request.method == 'GET':
        context = {'error' : False, 'message':""}
        return render(request, 'Users/signup.html', context)

def redir(request):
    response = redirect('/user/login')
    return response
