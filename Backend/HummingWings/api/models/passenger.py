""" Contains the Passenger model """
from django.db import models
from django_extensions.db.models import TimeStampedModel
from ..models.constants import _DOCUMENT_TYPE_CHOICES, _GENDER_CHOICES

class Passenger(TimeStampedModel):
    """ Passenger model definition. """
    _AGE_RANGE_CHOICES = [
        ('adulto', 'Adulto'),
        ('nino', 'Nino'),
        ('infante', 'Infante'),
    ]

    booking_holder = models.ForeignKey('BookingHolder', on_delete=models.CASCADE, related_name='passengers')
    first_name = models.CharField("Nombre(s)", max_length=255)
    last_name = models.CharField("Apellido(s)", max_length=255)
    email = models.EmailField()
    age_range = models.CharField(max_length=8, choices=_AGE_RANGE_CHOICES)
    gender = models.CharField(max_length=10, choices=_GENDER_CHOICES)
    birth_date = models.DateField("Fecha de Nacimiento", 
        null=True, blank=True)
    document_type = models.CharField("Tipo de documento", max_length=255,
        choices=_DOCUMENT_TYPE_CHOICES, default="C.C.")
    document = models.CharField("Identificación", max_length=255, unique=True)
    cellphone = models.CharField("Celular", max_length=10, null=True, blank=True, default=None),
    seat_code = models.CharField("Codigo de asiento", max_length=2)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        """ Sets human readable name """
        db_table = "Passenger"
        verbose_name = "Passenger"
        verbose_name_plural = "Passengers"