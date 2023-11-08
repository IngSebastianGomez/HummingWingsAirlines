
import random

from ..models.constants import CLIENT


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
            "owner": {"required": True, "type": "integer", "min": 1},
            "number": {"required": True, "type": "string", "min-length":16},
            "date_expire": {"required": True, "type": "string", "regex": DATE_REGEX},
            "code_secure": {"required": True, "type": "string", "min-length": 3}
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

        request.data["owner"] = User.objects.filter(
            pk=request.data["owner"], rol=CLIENT).first()

        request.data["cash"] = random.randint(1000000,15000000)
        card = Card.objects.create(**request.data)

        return Response({
            "inserted": card.pk
        }, status=status.HTTP_201_CREATED)


class SpecificCardApi(APIView, TokenHandler):
    """ Contains specific card management methods """

    def delete(self, request, card_pk):
        """ deletes a specific card

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        card_pk: string
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

        card = Card.objects.filter(owner__pk=user.pk, pk=card_pk).first()
        if not card:
            return Response({
                "code": "card_not_found",
                "detailed": "No existe una tarjeta con ese id"
            }, status=status.HTTP_404_NOT_FOUND)

        card.delete()
        return Response({
            "deleted": card_pk,
            "code": "card_deleted",
            "detailed": "Tarjeta eliminado correctamente"
        }, status=status.HTTP_200_OK)
