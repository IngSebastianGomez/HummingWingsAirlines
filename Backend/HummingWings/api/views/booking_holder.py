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
            "only_booking_holder": {"required": True, "type": "boolean"},
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
                        "seat_code": {"required": True, "type": "string", "regex": r"^[1-17][A-E]$"}
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

        booking_holder = BookingHolder.objects.create(
            user=user,
            email=request.data["email"],
            cellphone=request.data["cellphone"],
            flight=request.data["flight"]
        )

        for passenger_data in request.data["passengers"]:
            passenger_data["booking_holder"] = booking_holder.id
            passenger_data["cellphone"] = passenger_data.get("cellphone", None)
            passenger_data["birth_date"] = timezone.datetime.strptime(
                passenger_data["birth_date"]).date()
            Passenger.objects.create(**passenger_data)

        data = {"inserted": booking_holder.id}

        if not request.data["only_booking_holder"]:
            payment_log = PaymentLog.objects.create(
                booking_holder=booking_holder,
                amount=booking_holder.get_payment_price(),
                tickets_amount=booking_holder.get_passengers_amount()
            )
            data["payment_log"] = payment_log.id

        return Response(data, status=status.HTTP_201_CREATED)
