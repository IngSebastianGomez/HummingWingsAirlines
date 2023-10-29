"""Contains the flights model"""
from django.db import models
from datetime import datetime, timedelta
from constants import _TYPE_FLIGHT_CHOICES

class Flights(models.Model):
    code_flight = models.AutoField(primary_key=True)
    city_start = models.CharField(max_length=100)
    city_end = models.CharField(max_length=100)
    price_of_ticket = models.DecimalField(max_digits=10, decimal_places=2)
    hour_start = models.TimeField()
    hour_end = models.TimeField()
    is_international = models.BooleanField(default=False)

    type_flight = models.CharField(
        max_length=10,
        choices=_TYPE_FLIGHT_CHOICES,
        default='directo'
    )

    def time_of_flight(self):
        """Returns the total time of flight"""
        time_flight = self.hour_end - self.hour_start
        return time_flight


    def __str__(self):
        return f"Vuelo de {self.city_start} a {self.city_end}"
    
    class Meta:
        """ Sets human readable name """
        db_table = "Flights"
        verbose_name = "Flight"
        verbose_name_plural = "Flights"