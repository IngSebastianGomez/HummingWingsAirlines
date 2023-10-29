from django.db import models

class BookingHolder(models.Model):
    email = models.EmailField(unique=True, verbose_name="Correo")
    cellphone = models.CharField(max_length=255, verbose_name="Celular")
    tickets_pending = models.ManyToManyField('api.Ticket', related_name='booking_holders', blank=True)

    def __str__(self):
        return f"Booking Holder: {self.email}"
    
    class Meta:
        """ Sets human readable name """
        db_table = "BookingHolders"
        verbose_name = "BookingHolder"
        verbose_name_plural = "BookingHolders"
