""" Contains User endpoint management definition """

import datetime as dt
import random
from cerberus import Validator
from django.contrib.auth.hashers import make_password
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers.userSerializer import UserSerializer

from ..helpers.token import TokenHandler
from ..helpers.email import send_template_email
from ..helpers.envs import getenv

from ..models.email_template import CLIENT_REGISTER_CONFIRMATION
from ..models.constants import _GENDER_CHOICES, _STATUS_400_MESSAGE, _STATUS_401_MESSAGE, _STATUS_CHOICES, _TYPE_DOCUMENT_CHOICES, APPROVED
from ..models.constants import _USER_ROL_CHOICES, PENDING, ADMIN, CLIENT 
from ..models.user import User


class UserApi(APIView, TokenHandler):
    """ Defines the HTTP verbs to user model management """

    def post(self, request): 
        """ Creates a new user.

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
            "first_name": {"required": True, "type": "string"},
            "last_name": {"required": True, "type": "string"},
            "birth_date": {
                "required": True, "type": "string", 
                "regex": r"((19[0-9]{2}|20[0-9]{2})-([0][1-9]|[1][0-2])-"
                        r"(10|20|[0-2][1-9]|[3][0-1]))"},
            "email": {"required": True, "type": "string"},
            "rol": {
                "required": True, "type": "string",
                "allowed": [item[0] for item in _USER_ROL_CHOICES]
            },
            "document_type": {
                "required": True, "type": "string",
                "allowed": [item[0] for item in _TYPE_DOCUMENT_CHOICES]
            },
            "document": {"required": True, "type": "string", "regex": r"^\d*$"},
            "address": {"required": True, "type": "string"},
            "cellphone": {"required": True, "type": "string", "minlength": 10},
            "gender": {
                "required": True, "type": "string",
                "allowed": [item[0] for item in _GENDER_CHOICES]
            },
            "password": {
                "required": True, "type": "string",
                "regex": r'^.*(?=.{8,100})(?=.*[a-zA-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z0-9].*$'},
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        if not is_adult(request.data["birth_date"]):
            return Response({
                "code": "invalid_birth_date",
                "detailed": "El usuario debe ser mayor de edad"
            }, status=status.HTTP_400_BAD_REQUEST)

        client = User.objects.filter(
            Q(document=request.data["document"]) | Q(email=request.data["email"]))
        if client:
            return Response({
                "code": "integrity_error",
                "detailed": "Ya existe un usuario registrado con ese documento o email"
            }, status=status.HTTP_409_CONFLICT)

        request.data["token"] = random.randint(0000, 9999)
        request.data["password"] = make_password(request.data["password"])

        client = User.objects.create(**request.data)

        send_template_email(
            email_id=CLIENT_REGISTER_CONFIRMATION,
            params={
                "full_name": client.get_full_name,
                "url": f"{getenv('API_HOSTNAME')}/api/v1/user/{client.pk}/confirm_email/{client.token}"
            },
            receivers=client.email,
            tracking_dict={
                "id_module": client.pk,
                "type_module": CLIENT
            }
        )
        return Response({
            "inserted": client.pk
        }, status=status.HTTP_201_CREATED)


    def get(self, request):
        """ Gets all users.

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
            "rol": {"required": False, "type": "string", "allowed": _USER_ROL_CHOICES},
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        payload, user = self.get_payload(request)
        if not payload or user.rol != ADMIN or user.status == PENDING:
            return Response({
                "code": "do_not_have_permission",
                "detailed": "Sólo los administradores activos pueden listar los usuarios"
            }, status=status.HTTP_401_UNAUTHORIZED)

        users = User.objects.filter(rol=CLIENT)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SpecificClientApi(APIView, TokenHandler):
    """ Defines the http verbs to specific client management """

    def get(self, request, client_pk):
        """ Gets an specific client

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        client_pk: int
            Pk of specific client

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        payload, user = self.get_payload(request)
        if (
            (not payload or not user) or 
            (user.status == PENDING and user.rol != ADMIN)
        ):
            return Response({
                "code": "do_not_have_permission",
                "detailed": "No tienes permisos para realizar esta acción"
            }, status=status.HTTP_401_UNAUTHORIZED)

        client = User.objects.filter(pk=client_pk).first()
        if not client:
            return Response({
                "code": "user_not_found",
                "detailed": "No existe un usuario con ese id"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, client_pk):
        """ Updates an specific client

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        client_pk: int
            Pk of specific client

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        validator = Validator({
            "first_name": {"required": False, "type": "string"},
            "last_name": {"required": False, "type": "string"},
            "email": {"required": False, "type": "string"},
            "address": {"required": False, "type": "string"},
            "cellphone": {"required": False, "type": "string", "minlength": 10},
            "gender": {
                "required": False, "type": "string",
                "allowed": [item[0] for item in _GENDER_CHOICES]
            },
            "password": {
                "required": False, "type": "string",
                "regex": r'^.*(?=.{8,100})(?=.*[a-zA-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z0-9].*$'},
            "token": {
                "required": False, "type": "integer", 
                "dependencies": "password"
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
            (not payload or not user) or
            (
                (user.status == PENDING or user.pk != client_pk)
                and user.rol != ADMIN
            )
        ):
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)

        client = User.objects.filter(pk=client_pk)
        if not client:
            return Response({
                "code": "user_not_found",
                "detailed": "No existe un usuario con ese id"
            }, status=status.HTTP_404_NOT_FOUND)

        data = {}
        if "email" in request.data:
            data["email"] = request.data["email"]
        if "first_name" in request.data:
            data["first_name"] = request.data["first_name"]
        if "last_name" in request.data:
            data["last_name"] = request.data["last_name"]
        if "address" in request.data:
            data["address"] = request.data["address"]
        if "cellphone" in request.data:
            data["cellphone"] = request.data["cellphone"]
        if "gender" in request.data:
            data["gender"] = request.data["gender"]
        if "password" in request.data and request.data["token"] == client.token:
            data["password"] = make_password(request.data["password"])
        elif request.data["token"] != client.token:
            return Response({
                "code": "invalid_token",
                "detailed": "El token es inválido"
            }, status=status.HTTP_400_BAD_REQUEST)

        client.update(**data)
        return Response({
            "code": "client_updated",
            "detailed": "Usuario actualizado correctamente"
        }, status=status.HTTP_200_OK)


    def delete(self, request, client_pk):
        """ Deletes an specific client

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        client_pk: int
            Pk of specific client

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        payload, user = self.get_payload(request)
        if not payload or user.status == PENDING or user.pk != client_pk:
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)

        user.delete()
        return Response({
            "code": "client_deleted",
            "detailed": "Usuario eliminado correctamente"
        }, status=status.HTTP_200_OK)


class ConfirmRegisterApi(APIView, TokenHandler):
    """ Defines the http verbs to confirm register management """

    def get(self, request, pk, token):
        """ Confirms the register of an specific client

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        client_pk: int
            Pk of specific user
            
        token: int
            Token to confirm the register

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        user = User.objects.filter(pk=pk, token=token).first()
        if not user:
            return Response({
                "code": "invalid_token",
                "detailed": "El token es inválido"
            }, status=status.HTTP_400_BAD_REQUEST)

        user.status = APPROVED
        user.token = random.randint(0000, 9999)
        user.save()
        return Response({
            "code": "user_approved",
            "detailed": "Usuario aprobado correctamente"
        }, status=status.HTTP_200_OK)


##### Functions #####
def is_adult(birth_date):
    """ Calculates if the user is adult

    Parameters
    ----------

    birth_date: str
        Contains the birth date of the user

    Returns
    -------

    result: boolean
        True if the user is adult or False if the user is not adult

    """
    birth_date = dt.datetime.strptime(birth_date, "%Y-%m-%d")
    today = dt.datetime.today()
    return (
        (today.year - birth_date.year - 
         ((today.month, today.day) < (birth_date.month, birth_date.day))
        ) >= 18
    )
