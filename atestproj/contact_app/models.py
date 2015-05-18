from django.db import models

# Create your models here.

class Contact(models.Model):
	firstname 	= models.CharField(max_length=25)
	lastname 	= models.CharField(max_length=25)

