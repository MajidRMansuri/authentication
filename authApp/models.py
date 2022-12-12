from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    locality = models.TextField()
    country = models.TextField()
    state = models.TextField()
    city = models.TextField()
    zipcode = models.IntegerField()
    language = models.BooleanField()
