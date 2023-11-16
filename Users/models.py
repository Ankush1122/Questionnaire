from django.db import models

class Credentials(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_credential = models.ForeignKey(Credentials, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
