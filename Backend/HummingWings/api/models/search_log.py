"""Contains the Search Log model"""
from django.db import models
from django_extensions.db.models import TimeStampedModel
from datetime import datetime, timedelta

from ..models.constants import _TYPE_FLIGHT_CHOICES, DIRECT
from ..models.seat import Seat


class SearchLog(TimeStampedModel):
    """ SearchLog model definition. """
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="search_log")
    ip = models.CharField("Dirección Ip", max_length=50, null=True, blank=True)
    city_start = models.CharField("Ciudad origen", max_length=100)
    city_end = models.CharField("Ciudad destino", max_length=100)
    date_start = models.DateTimeField("Fecha de salida")

    def __str__(self):
        return f"{self.pk}. Historial de {self.user}: {self.city_start} a {self.city_end}"

    class Meta:
        """ Sets human readable name """
        db_table = "Search"
        verbose_name = "Search"
        verbose_name_plural = "Searchs"
