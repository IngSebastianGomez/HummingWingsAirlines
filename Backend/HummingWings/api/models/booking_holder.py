from django.db import models
from ticket import Ticket

class BookingHolder(models.Model):
    email = models.EmailField()
    cellphone = models.CharField(max_length=20)
    tickets_pending = models.ManyToManyField(Ticket, related_name='booking_holders', blank=True)

    def __str__(self):
        return f"Booking Holder: {self.email}"
    
    class Meta:
        """ Sets human readable name """
        db_table = "BookingHolders"
        verbose_name = "BookingHolder"
        verbose_name_plural = "BookingHolders"    