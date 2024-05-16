from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200,)
    email= models.CharField(max_length=200)
    password =models.CharField(max_length=200,)
    # Add additional fields for user profile (if needed)
    # Example:
    # bio = models.TextField(max_length=500, blank=True)
    def __str__(self):
	    return self.username
