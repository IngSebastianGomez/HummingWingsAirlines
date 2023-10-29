from django.db import models

class Cards(models.Model):
    owner = models.CharField("Propietario", max_length=100, blank=False, null=False)
    number = models.CharField("Numero de tarjeta", max_length=16, null=False, blank=False)
    date_expire = models.DateField("Fecha de vencimiento", null=False, blank=False)
    code_secure = models.CharField("Codigo de seguridad", max_length=3, null=False, blank=False)
    cash = models.DecimalField("Saldo", max_digits=10, decimal_places=2)
    date_create = models.DateTimeField("Fecha de creacion", auto_now_add=True)

    def __str__(self):
        return f'Tarjeta de {self.owner}'

    class Meta:
        db_table = "Tarjetas"
        verbose_name = "Tarjeta"
        verbose_name_plural = "Tarjetas"
