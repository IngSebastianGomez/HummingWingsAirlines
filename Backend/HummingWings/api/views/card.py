""" Contains Card model management views """

from decimal import Decimal
import random
from cerberus import Validator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from ..helpers.token import TokenHandler

from ..models.card import Card
from ..models.constants import _STATUS_400_MESSAGE, _STATUS_401_MESSAGE, CLIENT, DATE_REGEX
from ..models.user import User


class CardApi(APIView, TokenHandler):
    """ Contains Card model management """

    def post(self, request):
        """ Crates a new Card

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
            "code_secure": {"required": True, "type": "string"},
            "date_expire": {"required": True, "type": "string"},
            "number": {"required": True, "type": "string"},
            "owner": {"required": True, "type": "integer", "min": 1}
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

        if Card.objects.filter(number=request.data["number"]).exists():
            return Response({
                "code": "card_already_exists",
                "detailed": "Ya existe una tarjeta con ese número"
            }, status=status.HTTP_400_BAD_REQUEST)

        if request.data["date_expire"] < timezone.now().strftime("%Y-%m-%d"):
            return Response({
                "code": "invalid_date",
                "detailed": "La fecha de expiración no puede ser menor a la actual"
            }, status=status.HTTP_400_BAD_REQUEST)

        request.data["owner"] = User.objects.filter(
            pk=request.data["owner"], rol=CLIENT).first()

        if not request.data["owner"]:
            return Response({
                "code": "owner_not_found",
                "detailed": "No existe un usuario con ese id"
            }, status=status.HTTP_404_NOT_FOUND)

        request.data["cash"] = Decimal(random.randint(1000000,15000000))
        card = Card.objects.create(**request.data)

        return Response({
            "inserted": card.pk
        }, status=status.HTTP_201_CREATED)


class SpecificCardApi(APIView, TokenHandler):
    """ Contains specific card management methods """

    def delete(self, request, card_id):
        """ deletes a specific card

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        card_id: string
            PK of the card

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        payload, user = self.get_payload(request)
        if (
            not payload or not user or not isinstance(user, User)
            and user.rol == CLIENT
        ):
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)

        card = Card.objects.filter(owner__pk=user.pk, pk=card_id).first()
        if not card:
            return Response({
                "code": "card_not_found",
                "detailed": "No existe una tarjeta con ese id"
            }, status=status.HTTP_404_NOT_FOUND)

        card.delete()
        return Response({
            "deleted": card_id,
            "code": "card_deleted",
            "detailed": "Tarjeta eliminado correctamente"
        }, status=status.HTTP_200_OK)
