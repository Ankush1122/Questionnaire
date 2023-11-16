from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")
    #return render(request, 'Home/home.html')

def redir(request):
    response = redirect('/home/')
    return response
