""" Contains Flight endpoint management definition """

import datetime as dt
from cerberus import Validator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..helpers.token import TokenHandler

from ..models.constants import _STATUS_400_MESSAGE, _STATUS_401_MESSAGE, ADMIN
from ..models.user import User


class FlightApi(APIView, TokenHandler):
    """ Contains all the verbs for the flight API """

    def get(self, request):
        """ Gets all the flights

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
            "city_from": {"required": False, "type": "string"},
            "city_to": {"required": False, "type": "string"},
            "date_from": {"required": False, "type": "string"}
        })
        if not validator.validate(request.GET):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        payload, user = self.get_payload(request)
        if not payload or not isinstance(user, User) or user.rol != ADMIN:
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)

        query = {}
        if "city_from" in request.GET:
            query["city_from__icontains"] = request.GET["city_from"]
        if "city_to" in request.GET:
            query["city_to__icontains"] = request.GET["city_to"]
        if "date_from" in request.GET:
            query["date_from__gte"] = request.GET["date_from"]

        flights = Flight.objects.filter(**query).all()

        return Response({
            "count": flights.count(),
            "data": FlightSerializer(flights, many=True).data
        }, status=status.HTTP_200_OK)


    def post(self, request):
        """ Creates a new flight

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
            "departure_time": {"required": True, "type": "string"},
            "hours_of_flight": {"required": True, "type": "integer"},
            "price": {"required": True, "type": "integer"}
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        payload, user = self.get_payload(request)
        if not payload or not isinstance(user, User) or user.rol != ADMIN:
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)

        if (
            Flight.objects.filter(
                city_from=request.GET["city_from"],
                city_to=request.GET["city_to"],
                date_from=request.GET["date_from"],
                departure_time=request.GET["departure_time"]).exists()
        ):
            return Response({
                "code": "flight_already_exists",
                "detailed": "El vuelo ya existe"
            }, status=status.HTTP_409_CONFLICT)

        request.GET["arrival_time"] = dt.datetime.strptime(
            request.GET["departure_time"], "%H:%M:%S"
        ) + dt.timedelta(hours=request.GET["hours_of_flight"])

        request.GET["date_to"] = dt.datetime.strptime(
            request.GET["date_from"], "%Y-%m-%d"
        ) + dt.timedelta(days=request.GET["hours_of_flight"]%24)

        request.GET.pop("hours_of_flight")

        flight = Flight.objects.create(**request.GET)

        ## Hay que revisarlo
        New.objects.create(
            user=user,
            flight=flight,
            date=dt.datetime.now()
        )

        return Response({
            "inserted": flight.pk
        }, status=status.HTTP_201_CREATED)


class SpecificFlightApi(APIView, TokenHandler):
    """ Contains all the verbs for the specific flight API """

    def get(self, request, flight_id):
        """ Gets a specific flight

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        flight_id: int
            Flight id

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        payload, user = self.get_payload(request)
        if not payload or not isinstance(user, User) or user.rol != ADMIN:
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)

        flight = Flight.objects.filter(pk=flight_id).first()
        if not flight:
            return Response({
                "code": "flight_not_found",
                "detailed": "El vuelo no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "data": FlightSerializer(flight).data
        }, status=status.HTTP_200_OK)


    def patch(self, request, flight_id):
        """ Updates a specific flight

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        flight_id: int
            Flight id

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        validator = Validator({
            "city_from": {"required": False, "type": "string"},
            "city_to": {"required": False, "type": "string"},
            "date_from": {"required": False, "type": "string"},
            "departure_time": {"required": False, "type": "string"},
            "hours_of_flight": {"required": False, "type": "integer"},
            "price": {"required": False, "type": "integer"}
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        payload, user = self.get_payload(request)
        if not payload or not isinstance(user, User) or user.rol != ADMIN:
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)

        flight = Flight.objects.filter(pk=flight_id).first()
        if not flight:
            return Response({
                "code": "flight_not_found",
                "detailed": "El vuelo no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        if flight.has_sold_tickets():
            return Response({
                "code": "flight_has_sold_tickets",
                "detailed": "El vuelo ya tiene tickets vendidos"
            }, status=status.HTTP_409_CONFLICT)

        Flight.objects.filter(pk=flight_id).update(**request.data)

        return Response({
            "updated": flight_id
        }, status=status.HTTP_200_OK)


    def delete(self, request, flight_id):
        """ Deletes a specific flight

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        flight_id: int
            Flight id

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        payload, user = self.get_payload(request)
        if not payload or not isinstance(user, User) or user.rol != ADMIN:
            return Response({
                "code": "do_not_have_permission",
                "detailed": "No tienes permiso para ejecutar esta acción"
            }, status=status.HTTP_401_UNAUTHORIZED)

        flight = Flight.objects.filter(pk=flight_id).first()
        if not flight:
            return Response({
                "code": "flight_not_found",
                "detailed": "El vuelo no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        if flight.has_sold_tickets():
            return Response({
                "code": "flight_has_sold_tickets",
                "detailed": "El vuelo ya tiene tickets vendidos"
            }, status=status.HTTP_409_CONFLICT)

        flight.delete()

        return Response({
            "deleted": flight_id
        }, status=status.HTTP_200_OK)
