'''Contain the payment log model'''
from django.db import models
from django_extensions.db.models import TimeStampedModel

from ..models.constants import _STATUS_CHOICES, PENDING


class PaymentLog(TimeStampedModel):
    """ Payment log model definition. """

    booking_holder = models.ForeignKey("BookingHolder", on_delete=models.CASCADE, related_name="payment_log")
    card = models.ForeignKey("Card", on_delete=models.CASCADE, related_name="payment_log", null=True)
    tickets_amount = models.IntegerField("Cantidad de tiquetes")
    amount = models.DecimalField("Valor del pago", max_digits=10, decimal_places=2)
    payment_status = models.CharField("Estado de pago", choices=_STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.pk}. {self.tickets}"

    class Meta:
        """ Sets human readable name """
        db_table = "Payment_logs"
        verbose_name = "Payment log"
        verbose_name_plural = "Payment logs"

    def get_tickets(self):
        """ Get all tickets related to this payment log """
        return self.tickets.all()
