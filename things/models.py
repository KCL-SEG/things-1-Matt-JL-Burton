from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):  

    def validate_quantity_range(value):
        if value < 0 or value > 100:
            raise ValidationError('Quantity must be between 0 and 100.')

    name = models.CharField(max_length=30, unique=True, blank=False)
    username = models.CharField(max_length=30, unique=True, blank=False)
    description=models.CharField(unique=False, blank=True,max_length=120)
    quantity = models.IntegerField(unique=False, blank=False, validators=[validate_quantity_range])
    password = models.CharField(unique=True, blank=False, max_length=30)


# Create your models here.


