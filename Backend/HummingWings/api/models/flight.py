"""Contains the flight model"""
from django.db import models
from django_extensions.db.models import TimeStampedModel
from datetime import datetime, timedelta

from ..models.constants import _TYPE_FLIGHT_CHOICES, DIRECT, FIRST_CLASS
from ..models.seat import Seat
from ..models.ticket import Ticket


class Flight(TimeStampedModel):
    """ Flight model definition. """
    code_flight = models.AutoField("Codigo de vuelo", primary_key=True)
    city_start = models.CharField("Ciudad origen", max_length=100)
    city_end = models.CharField("Ciudad destino", max_length=100)
    price_of_ticket = models.DecimalField("Precio del ticket", max_digits=10, decimal_places=2)
    date_start = models.DateTimeField("Fecha de salida")
    date_end = models.DateTimeField("Fecha de llegada")
    is_international = models.BooleanField("Es internacional", default=False)
    available_seats = models.IntegerField("Asientos disponibles", default=0)
    type_flight = models.CharField("Tipo de vuelo", max_length=10,
        choices=_TYPE_FLIGHT_CHOICES,default=DIRECT)

    def __str__(self):
        return f"Code: {self.code_flight} Vuelo de {self.city_start} a {self.city_end}"

    class Meta:
        """ Sets human readable name """
        db_table = "Flight"
        verbose_name = "Flight"
        verbose_name_plural = "Flights"

    def time_of_flight(self):
        """Returns the number of hours between two datetime objects"""
        time_difference = self.date_end - self.date_start
        hours = time_difference.total_seconds() / 3600
        return hours

    def has_sold_seats(self):
        """ Returns if the flight has sold seats """
        return Seat.objects.filter(flight__pk=self.pk).exists()

    def has_sold_tickets(self):
        """ Returns if the flight has sold tickets """
        return Ticket.objects.filter(flight__pk=self.pk).exists()

    def update_seats(self):
        """ Updates the available seats of the flight """
        self.available_seats = Seat.objects.filter(flight__pk=self.pk).count()
        self.save()

    def get_sold_seats(self):
        """ Returns the sold seats of the flight """
        seats = Seat.objects.filter(flight__pk=self.pk).all()
        return [seat.code_seat() for seat in seats]

    def get_available_seat(self, seat_code):
        """ Returns a seat with given code """
        if Seat.objects.filter(flight__pk=self.pk, code_seat=seat_code).exists():
            return None
        class_flight = "Primera" if seat_code[:-1] in FIRST_CLASS else "General"
        type_location = (
            "Ventana" if seat_code[-1] in "AF" else
            "Centro" if seat_code[-1] in "BE" else
            "Pasillo"
        )
        seat = Seat.objects.create(
            flight=self,
            class_flight=class_flight,
            type_location=type_location,
            row=seat_code[:-1],
            column=seat_code[-1],
        )
        self.update_seats()
        return seat
