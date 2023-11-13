""" Contains Flight public search endpoints definition"""

from cerberus import Validator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..helpers.token import TokenHandler

from ..models.constants import _STATUS_400_MESSAGE, ONE_WAY, ROUND_TRIP


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
            "city_from": {"required": True, "type": "string"},
            "city_to": {"required": True, "type": "string"},
            "date_from": {"required": True, "type": "string"},
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
                city_from=request.GET["city_from"],
                city_to=request.GET["city_to"]
            )

        query = {
            "city_from__icontains": request.GET["city_from"],
            "city_to__icontains": request.GET["city_to"],
            "date_from__gte": request.GET["date_from"],
            "avaliable_seats__gt": request.GET["seats"]
        }

        flights = Flight.objects.filter(**query).all()

        return Response({
            "count": flights.count(),
            "data": PublicFlightSerializer(flights, many=True).data
        }, status=status.HTTP_200_OK)
