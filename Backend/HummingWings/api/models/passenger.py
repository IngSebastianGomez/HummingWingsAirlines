""" Contains the Passenger model """
from django.db import models
from django_extensions.db.models import TimeStampedModel
from ..models.constants import _GENDER_CHOICES

class Passenger(TimeStampedModel):
    """ Passenger model definition. """
    _AGE_RANGE_CHOICES = [
        ('adulto', 'Adulto'),
        ('nino', 'Nino'),
        ('infante', 'Infante'),
    ]
    
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    age_range = models.CharField(max_length=8, choices=_AGE_RANGE_CHOICES)
    gender = models.CharField(max_length=10, choices=_GENDER_CHOICES)

    def __str__(self):
        return self.full_name

    class Meta:
        """ Sets human readable name """
        db_table = "Passenger"
        verbose_name = "Passenger"
        verbose_name_plural = "Passengers"