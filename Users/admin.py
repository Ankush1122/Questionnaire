from django.contrib import admin

from . import models

admin.site.register(models.Credentials)
admin.site.register(models.Users)
