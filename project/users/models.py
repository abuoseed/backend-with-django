from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=False, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    