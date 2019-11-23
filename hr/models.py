from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=50, unique=True)
    mobile = models.CharField(max_length=10, null=True)
    profile = models.CharField(max_length=100, null=True)
