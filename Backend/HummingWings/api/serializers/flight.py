""" Contains the serializers definition for Flight model """

from rest_framework import serializers

from ..models.flight import Flight
from ..models.seat import Seat


class FlightSerializer(serializers.ModelSerializer):

    hours_of_flight = serializers.SerializerMethodField("get_hours_of_flight")
    sold_seats = serializers.SerializerMethodField("get_sold_seats")

    class Meta:
        model = Flight
        fields = [
            "code_flight",
            "city_start",
            "city_end",
            "price_of_ticket",
            "date_start",
            "date_end",
            "is_international",
            "type_flight",
            "hours_of_flight",
            "sold_seats"
        ]

    def get_hours_of_flight(self, obj):
        return obj.time_of_flight()

    def get_sold_seats(self, obj):
        seat = Seat.objects.filter(
            flight__pk=obj.pk).values("row","column").first()
        return seat.code_seat() if seat else None

class PublicFlightSerializer(serializers.ModelSerializer):

    hours_of_flight = serializers.SerializerMethodField("get_hours_of_flight")
    sold_seats = serializers.SerializerMethodField("get_sold_seats")

    class Meta:
        model = Flight
        fields = [
            "code_flight",
            "city_start",
            "city_end",
            "price_of_ticket",
            "date_start",
            "date_end",
            "is_international",
            "type_flight",
            "hours_of_flight",
            "sold_seats"
        ]

    def get_hours_of_flight(self, obj):
        return obj.time_of_flight()

    def get_sold_seats(self, obj):
        """ Returns the sold seats of the flight """
        return obj.get_sold_seats()
