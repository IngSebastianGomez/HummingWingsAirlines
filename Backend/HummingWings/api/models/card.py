""" Contains the Card model """
from django.db import models
from django_extensions.db.models import TimeStampedModel

class Card(TimeStampedModel):
    """ Card Model definition. """
    owner = models.ForeignKey("User", related_name="card", on_delete=models.CASCADE)
    number = models.CharField("Numero de tarjeta", max_length=16, unique=True)
    date_expire = models.DateField("Fecha de vencimiento", null=False, blank=False)
    code_secure = models.CharField("Codigo de seguridad", max_length=3, null=False, blank=False)
    cash = models.DecimalField("Saldo", max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.pk}. Tarjeta de {self.owner}'

    class Meta:
        db_table = "Card"
        verbose_name = "Card"
        verbose_name_plural = "Cards"
