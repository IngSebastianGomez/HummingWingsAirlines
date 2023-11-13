'''Contain the ticket model'''
from django.db import models
from django_extensions.db.models import TimeStampedModel
from ..models.constants import _STATUS_CHOICES_TICKET, PENDING


class Ticket(TimeStampedModel):
    """ Ticket model definition. """
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE, related_name='passenger')
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='ticket')
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    code_booking = models.CharField(max_length=10, editable=False)
    status = models.CharField(max_length=10, choices=_STATUS_CHOICES_TICKET, default=PENDING)
    bookingholder = models.ForeignKey('BookingHolder', on_delete=models.CASCADE, related_name='booking_holder', blank=True)

    def __str__(self):
        return f"Tiquete para {self.passenger} en asiento {self.seat}"
    
    class Meta:
        """ Sets human readable name """
        db_table = "Tickets"
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
