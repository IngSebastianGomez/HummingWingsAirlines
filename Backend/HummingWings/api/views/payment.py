""" Contains Payment process view """
from decimal import Decimal
from cerberus import Validator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..helpers.email import send_template_email
from ..helpers.payment import create_ticket
from ..helpers.token import TokenHandler

from ..models.card import Card
from ..models.constants import _STATUS_400_MESSAGE, _STATUS_401_MESSAGE, APPROVED, CLIENT, DATE_REGEX, PENDING
from ..models.email_template import PAYMENT_CONFIRMATION_EMAIL, TICKET_CONFIRMATION_EMAIL
from ..models.payment_log import PaymentLog
from ..models.ticket import Ticket
from ..models.user import User


class PaymentApi(APIView, TokenHandler):
    """ Contains Payment model management """

    def post(self, request):
        """ Creates a new Payment

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
            "amount": {"required": True, "type": "float", "min": 0},
            "card_number": {"required": True, "type": "string"},
            "date_expire": {"required": True, "type": "string", "regex": DATE_REGEX},
            "cvv": {"required": True, "type": "string", "minlength": 3, "maxlength": 4},
            "payment_log": {"required": True, "type": "integer", "min": 1},
            "services": {
                "required": True, "type": "dict",
                "schema": {
                    "ticket": {
                        "required": False, "type": "dict",
                        "schema": {
                            "name": {"required": True, "type": "string"},
                            "cost": {"required": True, "type": "float", "min": 0}
                        }
                    },
                    "extraLuggage": {
                        "required": False, "type": "dict",
                        "schema": {
                            "name": {"required": True, "type": "string"},
                            "cost": {"required": True, "type": "float", "min": 0}
                        }
                    },
                    "bringPet": {
                        "required": False, "type": "dict",
                        "schema": {
                            "name": {"required": True, "type": "string"},
                            "cost": {"required": True, "type": "float", "min": 0}
                        }
                    },
                    "connectivityService": {
                        "required": False, "type": "dict",
                        "schema": {
                            "name": {"required": True, "type": "string"},
                            "cost": {"required": True, "type": "float", "min": 0}
                        }
                    },
                    "totalPrice": {
                        "required": False, "type": "dict",
                        "schema": {
                            "name": {"required": True, "type": "string"},
                            "cost": {"required": True, "type": "float", "min": 0}
                        }
                    },
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

        payment_log = PaymentLog.objects.select_related().filter(
            pk=request.data["payment_log"], payment_status=PENDING,
            amount=request.data["amount"]).first()
        if not payment_log:
            return Response({
                "code": "payment_log_not_found",
                "detailed": "Registro de pago no encontrado"
            }, status=status.HTTP_404_NOT_FOUND)

        card = Card.objects.filter(
            number=request.data["card_number"],
            date_expire=request.data["date_expire"],
            code_secure=request.data["cvv"],
            owner_pk=user.pk
        ).first()
        if not card:
            return Response({
                "code": "card_not_found",
                "detailed": "Tarjeta no encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        if card.cash < Decimal(request.data["amount"]):
            return Response({
                "code": "insufficient_cash",
                "detailed": "Saldo insuficiente"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        card.cash -= Decimal(request.data["amount"])
        card.save()
        payment_log.card = card
        payment_log.payment_status = APPROVED
        payment_log.save()
        payment_log.booking_holder.status = APPROVED
        payment_log.booking_holder.save()
        for passenger in payment_log.booking_holder.passengers.all():
            create_ticket(
                passenger=passenger, 
                flight=payment_log.booking_holder.flight, 
                payment_log=payment_log
            )

        tickets = Ticket.objects.filter(
            payment_log=payment_log, status=APPROVED).all()

        # MANDAR LA FACTURA
        send_template_email(
            email_id=PAYMENT_CONFIRMATION_EMAIL,
            params={
                "first_name": user.first_name,
                "last_name": user.last_name,
                "amount": payment_log.amount,
                "payment_log": payment_log.id
            },
            receivers=[user.email]
        )
        
        for ticket in tickets: 
            send_template_email(
                email_id=TICKET_CONFIRMATION_EMAIL,
                params={
                    "first_name": ticket.passenger.first_name,
                    "last_name": ticket.passenger.last_name,
                    "amount": payment_log.amount,
                    "payment_log": payment_log.id,
                    "booking_code": ticket.booking_code
                },
                receivers=[ticket.passenger.email],
            )

        return Response({
            "code": "payment_approved",
            "detailed": "Pago aprobado"
        }, status=status.HTTP_200_OK)
