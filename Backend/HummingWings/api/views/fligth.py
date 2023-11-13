""" Contains Flight endpoint management definition """

import datetime as dt
from cerberus import Validator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializer.flight import FlightSerializer

from ..helpers.envs import getenv
from ..helpers.token import TokenHandler

from ..models.constants import _STATUS_400_MESSAGE, _STATUS_401_MESSAGE, ADMIN
from ..models.flight import Flight
from ..models.new import New
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
            "city_start": {"required": False, "type": "string"},
            "city_end": {"required": False, "type": "string"},
            "date_start": {"required": False, "type": "string"}
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
        if "city_start" in request.GET:
            query["city_start__icontains"] = request.GET["city_start"]
        if "city_end" in request.GET:
            query["city_end__icontains"] = request.GET["city_end"]
        if "date_start" in request.GET:
            query["date_start__gte"] = request.GET["date_start"]

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
            "city_start": {"required": True, "type": "string"},
            "city_end": {"required": True, "type": "string"},
            "date_start": {"required": True, "type": "string"},
            "hours_of_flight": {"required": True, "type": "integer"},
            "price_of_ticket": {"required": True, "type": "integer"},
            "is_international": {"required": True, "type": "boolean"}
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
                city_start=request.GET["city_start"],
                city_end=request.GET["city_end"],
                date_start__lte=(
                    request.GET["date_start"] + dt.timedelta(
                        hours=getenv("LIMIT_HOURS_SAME_FLIGHT"))
                )).exists()
        ):
            return Response({
                "code": "flight_already_exists",
                "detailed": "El vuelo ya existe"
            }, status=status.HTTP_409_CONFLICT)

        request.GET["date_end"] = dt.datetime.strptime(
            request.GET["date_start"], "%Y-%m-%d-%H:%M"
        ) + dt.timedelta(hours=request.GET["hours_of_flight"])

        request.GET.pop("hours_of_flight")

        flight = Flight.objects.create(**request.GET)

        New.objects.create(
            title=f"Nuevo vuelo de {self.city_start} a {self.city_end}",
            content=(
                f"Disponible un super vuelo de {self.city_start} a "
                f"{self.city_end}, aprovecha esta oportunidad, por "
                f"tan solo {self.price_of_ticket} solo en "
                f"HummingWings tu aerolínea de confianza"""
            )
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
            "city_start": {"required": False, "type": "string"},
            "city_end": {"required": False, "type": "string"},
            "date_start": {"required": False, "type": "string"},
            "hours_of_flight": {"required": False, "type": "integer"},
            "price_of_ticket": {"required": False, "type": "integer"}
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
