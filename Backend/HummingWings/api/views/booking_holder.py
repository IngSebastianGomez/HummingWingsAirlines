""" Contains Booking Holder model management views """

from decimal import Decimal
import random
from cerberus import Validator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from ..helpers.token import TokenHandler

from ..models.booking_holder import BookingHolder
from ..models.constants import _STATUS_400_MESSAGE, _STATUS_401_MESSAGE, CLIENT, DATE_REGEX, PENDING
from ..models.passenger import Passenger
from ..models.payment_log import PaymentLog
from ..models.user import User
from ..models.flight import Flight

from ..serializers.booking_holder import BookingHolderSerializer


class BookingHolderApi(APIView, TokenHandler):
    """ Contains Ticket model management """

    def post(self, request):
        """ Crates a Booking Holder

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
            "flight": {"required": True, "type": "integer", "min": 1},
            "email": {"required": True, "type": "string"},
            "cellphone": {"required": True, "type": "string"},
            "status": {"required": True, "type": "string"},
            "passengers": {
                "required": True, "type": "list",
                "schema": {
                    "type": "dict",
                    "schema": {
                        "first_name": {"required": True, "type": "string"},
                        "last_name": {"required": True, "type": "string"},
                        "email": {"required": True, "type": "string"},
                        "cellphone": {"required": False, "type": "string"},
                        "document_type": {"required": True, "type": "string"},
                        "document": {"required": True, "type": "string"},
                        "gender": {"required": True, "type": "string"},
                        "age_range": {"required": True, "type": "string"},
                        "birth_date": {"required": True, "type": "string"},
                        "seat_code": {"required": True, "type": "string", "regex": r"(?:[1-9]|1[0-7])[A-E]"}
                    }
                }
            }
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        payload, user = self.get_payload(request)
        if (
            not payload or not user or not isinstance(user, User)
            and user.rol == CLIENT
        ):
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)
        if request.data["passengers"] == []:
            return Response({
                "code": "invalid_body",
                "detailed": "passengers is required"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        fligth_dont_exists = Flight.objects.filter(pk=request.data["flight"]).exists()
        if not fligth_dont_exists:
            return Response({
                "code": "flight_dont_exists",
                "detailed": "flight dont exists"
            }, status=status.HTTP_400_BAD_REQUEST)

        already_exists_seat = Passenger.objects.filter(
            seat_code=request.data["passengers"][0]["seat_code"]).exists()
        if already_exists_seat:
            return Response({
                "code": "seat_already_exists",
                "detailed": "seat is ocuped"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        already_exists_document = Passenger.objects.filter(
            document=request.data["passengers"][0]["document"]).exists()
        
        if already_exists_document:
            return Response({
                "code": "document_already_exists",
                "detailed": "document already exists"
            }, status=status.HTTP_400_BAD_REQUEST)

        fligth_obj = Flight.objects.get(pk=request.data["flight"])

        booking_holder = BookingHolder.objects.create(
            user=user,
            email=request.data["email"],
            cellphone=request.data["cellphone"],
            flight=fligth_obj
        )
        

        for passenger_data in request.data["passengers"]:
            passenger_data["booking_holder"] = booking_holder
            passenger_data["email"] = request.data["email"]
            passenger_data["birth_date"] = timezone.datetime.strptime(
                passenger_data["birth_date"],"%Y-%m-%d").date()
            Passenger.objects.create(**passenger_data)

        payment_log = PaymentLog.objects.create(
            booking_holder=booking_holder,
            amount=booking_holder.get_payment_price(),
            tickets_amount=booking_holder.get_passengers_amount()
        )

        return Response({
            "inserted": booking_holder.pk,
            "payment_log": payment_log.pk
        }, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        """ Returns all booking holders

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        booking_holders = BookingHolder.objects.all()
        serializer = BookingHolderSerializer(booking_holders, many=True)

        return Response({
            "booking_holders": serializer.data
        }, status=status.HTTP_200_OK)