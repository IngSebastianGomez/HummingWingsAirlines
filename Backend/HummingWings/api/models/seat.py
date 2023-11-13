""" Contains the Seat model """
from django.db import models


class Seat(models.Model):
    """ Seat model definition. """
    _CLASS_CHOICES = [
        ('Primera', 'Primera'),
        ('General', 'General'),
    ]
    _TYPE_LOCATION_CHOICES = [
        ('Ventana', 'Ventana'),
        ('Pasillo', 'Pasillo'),
        ('Centro', 'Centro'),
    ]
    _ROW_CHOICES = [(str(i), str(i)) for i in range(1, 17)]
    _COLUMN_CHOICES = [
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    flight = models.ForeignKey(
        "Flight", verbose_name="Codigo vuelo", on_delete=models.CASCADE)
    class_flight = models.CharField(
        "Clase del asiento",max_length=8, choices=_CLASS_CHOICES)
    type_location = models.CharField(
        "Tipo de locacion", max_length=8, choices=_TYPE_LOCATION_CHOICES)
    row = models.CharField("Fila", max_length=2, choices=_ROW_CHOICES)
    column = models.CharField("Columna", max_length=2, choices=_COLUMN_CHOICES)


    def code_seat(self):
        return f'{self.row}{self.column}'

    def __str__(self):
        return f'Asiento {self.code_seat()} ({self.class_flight}) en vuelo {self.flight.city_start} - {self.flight.city_end}'

    class Meta:
        """ Sets human readable name """
        db_table = "Seat"
        verbose_name = "Seat"
        verbose_name_plural = "Seats"