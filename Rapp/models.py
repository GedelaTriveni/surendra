from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
	c = [
		('0','Guest'),
		('1','Admin'),
	]
	role_type = models.CharField(max_length=5,choices=c,default='0')
	
class Slot(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	mail =  models.CharField(max_length=100,null=True,blank=True)

class Table(models.Model):
	usrname = models.CharField(max_length=100,null=True,blank=True)
	number = models.IntegerField()
	mobile = models.CharField(max_length=10,null=True,blank=True)
	date = models.DateField(max_length=100,null=True,blank=True)
	time = models.TimeField(max_length=100,null=True,blank=True)