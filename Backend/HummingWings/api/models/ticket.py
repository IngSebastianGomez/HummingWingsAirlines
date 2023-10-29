'''Contain the ticket model'''
from django.db import models
from seat import Seat
from django.utils.crypto import get_random_string

class Ticket(models.Model):
    _STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('accepted', 'Aceptado'),
        ('check-in', 'Check-in'),
    ]

    passenger = models.CharField(max_length=100)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    code_booking = models.CharField(max_length=10, unique=True, default=get_random_string, editable=False)
    status = models.CharField(max_length=10, choices=_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Tiquete para {self.passenger} en asiento {self.seat}"
    
    class Meta:
        """ Sets human readable name """
        db_table = "Tickets"
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
