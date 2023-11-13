"""Contains the flight model"""
from django.db import models
from django_extensions.db.models import TimeStampedModel
from datetime import datetime, timedelta
from ..models.constants import _TYPE_FLIGHT_CHOICES, DIRECT

class Flight(TimeStampedModel):
    """ Flight model definition. """
    code_flight = models.AutoField("Codigo de vuelo", primary_key=True)
    city_start = models.CharField("Ciudad origen", max_length=100)
    city_end = models.CharField("Ciudad destino", max_length=100)
    price_of_ticket = models.DecimalField("Precio del ticket", max_digits=10, decimal_places=2)
    hour_start = models.TimeField("Hora de salida")
    hour_end = models.TimeField("Hora de llegada")
    is_international = models.BooleanField("Es internacional", default=False)

    type_flight = models.CharField(
        "Tipo de vuelo",
        max_length=10,
        choices=_TYPE_FLIGHT_CHOICES,
        default=DIRECT
    )


    def time_of_flight(self):
        """Returns the total time of flight"""
        time_flight = self.hour_end - self.hour_start
        return time_flight


    def __str__(self):
        return f"Code: {self.code_flight} Vuelo de {self.city_start} a {self.city_end}"
    
    class Meta:
        """ Sets human readable name """
        db_table = "Flight"
        verbose_name = "Flight"
        verbose_name_plural = "Flights"