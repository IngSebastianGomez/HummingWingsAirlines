""" Contains the serializers definition for Flight model """

from rest_framework import serializers
from ..models.flight import Flight


class FlightSerializer(serializers.ModelSerializer):

    hours_of_flight = serializers.SerializerMethodField("get_hours_of_flight")
    sold_seats = serializers.SerializerMethodField("get_sold_seats")

     class Meta:
        model = Flight
        include = [
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


class PublicFlightSerializer(serializers.ModelSerializer):

    hours_of_flight = serializers.SerializerMethodField("get_hours_of_flight")
    sold_seats = serializers.SerializerMethodField("get_sold_seats")

    class Meta:
        model = Flight
        include = [
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
        return Seat.objects.filter(
            flight__pk=obj.pk).values("code_seat")
