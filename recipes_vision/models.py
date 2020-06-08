# from django.db import models
from mongoengine import *
import datetime
from django.db import models
# from djangotoolbox.fields import ListField
# Create your models here.

class MyRecipes(models.Model):
    name= models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    introduction= models.CharField(max_length=255)
    material= models.CharField(max_length=255)