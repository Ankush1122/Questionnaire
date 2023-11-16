from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),

    # redirect urls
    path('', views.redir, name="redir"),
    path('Home/', views.redir, name="redir"),
]
