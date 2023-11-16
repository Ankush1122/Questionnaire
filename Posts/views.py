from django.shortcuts import render, redirect
from django.http import HttpResponse


def posts(request):
    return HttpResponse("Posts Page")

    #return render(request, 'Home/home.html')
