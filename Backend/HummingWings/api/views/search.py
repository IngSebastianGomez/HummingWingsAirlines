""" Contains Flight public search endpoints definition"""

from cerberus import Validator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers.flight import PublicFlightSerializer

from ..helpers.token import TokenHandler

from ..models.constants import _STATUS_400_MESSAGE, ONE_WAY, ROUND_TRIP
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
            "date_start": {"required": True, "type": "string"},
            "seats": {"required": True, "type": "string"},
            "travel_type": {
                "required": True, "type": "string",
                "allowed": [ROUND_TRIP, ONE_WAY]
            }
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        payload, user = self.get_payload(request)
        if payload and user and isinstance(user, User):
            SearchLog.objects.create(
                user=user,
                ip=request.headers["ip"],
                city_start=request.GET["city_start"],
                city_end=request.GET["city_end"],
                date_start=request.GET["date_start"]
            )

        query = {
            "city_start__icontains": request.GET["city_start"],
            "city_end__icontains": request.GET["city_end"],
            "date_start__gte": request.GET["date_start"],
            "avaliable_seats__gt": request.GET["seats"]
        }

        flights = Flight.objects.filter(**query).order_by("-date_start").all()

        return Response({
            "count": flights.count(),
            "data": PublicFlightSerializer(flights, many=True).data
        }, status=status.HTTP_200_OK)
