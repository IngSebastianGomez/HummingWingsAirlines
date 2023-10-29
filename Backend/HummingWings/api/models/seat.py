from django.db import models
from flights import Flights
from ticket import Ticket

class Seat(models.Model):
    _FLIGHT_CHOICES = [(flight.id, flight.city_start + " - " + flight.city_end) for flight in Flights.objects.all()]
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

    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    class_flight = models.CharField(max_length=8, choices=_CLASS_CHOICES)
    type_location = models.CharField(max_length=8, choices=_TYPE_LOCATION_CHOICES)
    row = models.CharField(max_length=2, choices=_ROW_CHOICES)
    column = models.CharField(max_length=2, choices=_COLUMN_CHOICES)
    ticket_passenger = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, blank=True)

    def code_seat(self):
        return f'{self.row}{self.column}'

    def __str__(self):
        return f'Asiento {self.codigo_asiento()} ({self.class_flight}) en vuelo {self.flight.city_start} - {self.flight.city_end}'
    
    class Meta:
        """ Sets human readable name """
        db_table = "Seats"
        verbose_name = "Seat"
        verbose_name_plural = "Seats"