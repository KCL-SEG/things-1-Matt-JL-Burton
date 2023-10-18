from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


class Thing(Model):  

    def validate_quantity_range(value):
        if value <= 0 or value >= 100:
            raise ValidationError('Quantity must be between 0 and 100.')

    name = models.CharField(max_length=30, unique=True, blank=False)
    # username = models.CharField(max_length=30, unique=True, blank=False)
    description=models.CharField(unique=False, blank=True,max_length=120, name='description')
    quantity = models.IntegerField(unique=False, blank=False, validators=[MaxValueValidator(100, message=None), MinValueValidator(0,message=None)],name='quantity')
    # password = models.CharField(unique=True, blank=False, max_length=30)


# Create your Model here.


