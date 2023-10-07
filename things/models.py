from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    description=models.TextField()
    name = models.TextField()
    quantity = models.IntegerField()
# Create your models here.
