from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('posts/', include('Posts.urls')),
    path('user/', include('Users.urls')),
]
