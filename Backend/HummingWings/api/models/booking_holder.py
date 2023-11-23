""" Contains the BookingHolder model """
from django.db import models
from django_extensions.db.models import TimeStampedModel
from ..models.constants import _STATUS_CHOICES, PENDING

class BookingHolder(TimeStampedModel):
    """ BookingHolder model definition. """

    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='booking_holder', null=True)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='booking_holder')
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

    def get_payment_price(self):
        """ Get the price of the payment """
        passengers = self.passengers.all()
        price = len(passengers) * self.flight.price_of_ticket
        return price

    def get_passengers_amount(self):
        """ Get all tickets related to this booking holder """
        return self.passengers.count()
