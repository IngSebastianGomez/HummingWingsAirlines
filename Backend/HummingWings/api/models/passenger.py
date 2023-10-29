from django.db import models
from ..models.constants import _GENDER_CHOICES

class Passenger(models.Model):
    _AGE_RANGE_CHOICES = [
        ('adulto', 'Adulto'),
        ('nino', 'Nino'),
        ('infante', 'Infante'),
    ]
    
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    age_range = models.CharField(max_length=8, choices=_AGE_RANGE_CHOICES)
    gender = models.CharField(max_length=10, choices=_GENDER_CHOICES)
    
    tickets = models.ManyToManyField('Ticket', related_name='passengers', blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        """ Sets human readable name """
        db_table = "Passengers"
        verbose_name = "Passenger"
        verbose_name_plural = "Passengers"