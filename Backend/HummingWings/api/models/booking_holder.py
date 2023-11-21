""" Contains the BookingHolder model """
from django.db import models
from django_extensions.db.models import TimeStampedModel
from ..models.constants import _STATUS_CHOICES, PENDING

class BookingHolder(TimeStampedModel):
    """ BookingHolder model definition. """
    email = models.EmailField(verbose_name="Correo")
    cellphone = models.CharField(max_length=255, verbose_name="Celular")
    status = models.CharField(max_length=10, choices=_STATUS_CHOICES, default=PENDING)
    

    def __str__(self):
        return f"Booking Holder: {self.email}"
    
    class Meta:
        """ Sets human readable name """
        db_table = "BookingHolders"
        verbose_name = "BookingHolder"
        verbose_name_plural = "BookingHolders"
