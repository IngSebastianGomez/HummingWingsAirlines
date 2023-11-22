""" Contains Flight public search endpoints definition"""

from cerberus import Validator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from ..serializers.flight import PublicFlightSerializer

from ..helpers.token import TokenHandler

from ..models.constants import _STATUS_400_MESSAGE, DATE_REGEX, ONE_WAY, ROUND_TRIP
from ..models.flight import Flight
from ..models.search_log import SearchLog
from ..models.user import User


class PublicFlightApi(APIView, TokenHandler):
    """ Contains all the verbs for search"""

    def get(self, request):
        """ Gets all the flights for given filters

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        validator = Validator({
            "city_start": {"required": True, "type": "string"},
            "city_end": {"required": True, "type": "string"},
            "date_start": {"required": False, "type": "string"},
            "seats": {"required": False, "type": "string"},
            "travel_type": {
                "required": True, "type": "string",
                "allowed": [ROUND_TRIP, ONE_WAY]
            },
            "return_date": {
                "required": False, "type": "string",
                "dependencies": {"travel_type": [ROUND_TRIP]}
            }
        })
        if not validator.validate(request.GET):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        payload, user = self.get_payload(request)
        if payload and user and isinstance(user, User):
            SearchLog.objects.create(
                user=user,
                city_start=request.GET["city_start"],
                city_end=request.GET["city_end"],
                date_start=request.GET["date_start"]
            )

        if request.GET["travel_type"] == ROUND_TRIP:
            return_date = timezone.datetime.strptime(request.GET["return_date"], "%Y-%m-%d")
            query = {
                "city_start__icontains": request.GET["city_end"],
                "city_end__icontains": request.GET["city_start"],
                "date_start__gte": timezone.make_aware(return_date),
                "date_start__lte": (
                    timezone.make_aware(return_date) + timezone.timedelta(days=1)
                ),
                "available_seats__gt": request.GET["seats"]
            }

            if not Flight.objects.filter(**query).order_by("-date_start").exists():
                return Response({
                    "code": "return_flight_not_found",
                    "detail": "No se encontraron vuelos de regreso",
                }, status=status.HTTP_404_NOT_FOUND)

        date_start = timezone.datetime.strptime(request.GET["date_start"], "%Y-%m-%d")

        query = {
            "city_start__icontains": request.GET["city_start"],
            "city_end__icontains": request.GET["city_end"],
            "date_start__gte": timezone.make_aware(date_start),
            "date_start__lte": (
                timezone.make_aware(date_start) + timezone.timedelta(days=1)
            ),
            "available_seats__gt": request.GET["seats"]
        }

        flights = Flight.objects.filter(**query).order_by("-date_start").all()

        return Response({
            "count": flights.count(),
            "data": PublicFlightSerializer(flights, many=True).data
        }, status=status.HTTP_200_OK)
