from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
    name = models.CharField(max_length=30)
    description=models.TextField()
    quantity = models.IntegerField()
# Create your models here.
