from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description=models.TextField(max_length=120)
    quantity = models.IntegerField()
# Create your models here.
