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

from ..models.email_template import ADMIN_REGISTER_CONFIRMATION, CLIENT_REGISTER_CONFIRMATION
from ..models.constants import _GENDER_CHOICES, _STATUS_CHOICES, _DOCUMENT_TYPE_CHOICES, _USER_ROL_CHOICES
from ..models.constants import _STATUS_403_MESSAGE, _STATUS_400_MESSAGE, _STATUS_401_MESSAGE
from ..models.constants import APPROVED, PENDING, ADMIN, CLIENT
from ..models.root import Root
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
                "regex": r"(19[2-9]\d|20[0-1]\d|2023)-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])"
            },
            "email": {"required": True, "type": "string"},
            "rol": {
                "required": True, "type": "string",
                "allowed": [item[0] for item in _USER_ROL_CHOICES]
            },
            "document_type": {
                "required": True, "type": "string",
                "allowed": [item[0] for item in _DOCUMENT_TYPE_CHOICES]
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
                "regex": r'^.*(?=.{8,100})(?=.*[a-zA-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z0-9].*$'
            },
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
            "rol": {"required": False, "type": "string", "allowed": [item[0] for item in _USER_ROL_CHOICES]},
            "status": {"required": False, "type": "string", "allowed": [item[0] for item in _STATUS_CHOICES]},
            "document_type": {
                "required": False, "type": "string", 
                "allowed": [item[0] for item in _DOCUMENT_TYPE_CHOICES]
            },
            "document": {"required": False, "type": "string", "regex": r"^\d*$"},
            "email": {"required": False, "type": "string"},
            "first_name": {"required": False, "type": "string"},
            "last_name": {"required": False, "type": "string"}
        })
        if not validator.validate(request.GET):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        query = Q()

        payload, user = self.get_payload(request)
        if "rol" in request.GET and request.GET["rol"] == ADMIN:
            if not payload or not isinstance(user, Root):
                return Response({
                    "code": "do_not_have_permission",
                    "detailed": "Sólo el root puede listar los administradores"
                }, status=status.HTTP_401_UNAUTHORIZED)

            query.add(Q(rol=ADMIN), Q.AND)
        else:
            if not payload or user.rol != ADMIN or user.status == PENDING:
                return Response({
                    "code": "do_not_have_permission",
                    "detailed": "Sólo los administradores activos pueden listar los usuarios"
                }, status=status.HTTP_401_UNAUTHORIZED)

            query.add(Q(rol=CLIENT), Q.AND)

        if "status" in request.GET:
            query &= Q(status=request.GET["status"])
        if "document_type" in request.GET:
            query &= Q(document_type=request.GET["document_type"])
        if "document" in request.GET:
            query &= Q(document=request.GET["document"])
        if "email" in request.GET:
            query &= Q(email__icontains=request.GET["email"])
        if "first_name" in request.GET:
            query &= Q(first_name__icontains=request.GET["first_name"])
        if "last_name" in request.GET:
            query &= Q(last_name__icontains=request.GET["last_name"])

        users = User.objects.filter(query)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SpecificUserApi(APIView, TokenHandler):
    """ Defines the http verbs to specific user management """

    def get(self, request, user_pk):
        """ Gets an specific user

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        user_pk: int
            Pk of specific user

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        validator = Validator({
            "rol": {"required": True, "type": "string", "allowed": [item[0] for item in _USER_ROL_CHOICES]},
        })
        if not validator.validate(request.GET):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        payload, user = self.get_payload(request)
        if not payload or not user or not isinstance(user, User):
            return Response({
                "code": "do_not_have_permission",
                "detailed": "No tienes permisos para realizar esta acción"
            }, status=status.HTTP_401_UNAUTHORIZED)

        if request.GET["rol"] == ADMIN and user.rol != ADMIN:
            return Response({
                "code": "do_not_have_permission",
                "detailed": "Sólo los administradores pueden consultar otros administradores"
            }, status=status.HTTP_403_FORBIDDEN)

        user_consulted = User.objects.filter(pk=user_pk, rol=request.GET["rol"]).first()
        if not user_consulted:
            return Response({
                "code": "user_not_found",
                "detailed": "No existe un usuario con ese id"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user_consulted)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, user_pk):
        """ Updates an specific user

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        user_pk: int
            Pk of specific user

        Returns
        -------

        Response: (dict, int)
            Body response and status code.

        """
        validator = Validator({
            "rol": {"required": False, "type": "string", "allowed": [item[0] for item in _USER_ROL_CHOICES]},
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
                "regex": r'^.*(?=.{8,100})(?=.*[a-zA-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z0-9].*$'
            },
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
        if not payload or not user:
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)

        if request.data["rol"] == ADMIN and user.rol != ADMIN:
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_403_MESSAGE
            }, status=status.HTTP_403_FORBIDDEN)

        user_to_update = User.objects.filter(pk=user_pk, rol=request.data["rol"])
        if not user:
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
        if "password" in request.data and request.data["token"] == user_to_update.token:
            data["password"] = make_password(request.data["password"])
        elif request.data["token"] != user_to_update.token:
            return Response({
                "code": "invalid_token",
                "detailed": "El token es inválido"
            }, status=status.HTTP_400_BAD_REQUEST)

        user_to_update.update(**data)
        return Response({
            "updated": user_to_update.pk,
            "code": "user_updated",
            "detailed": "Usuario actualizado correctamente"
        }, status=status.HTTP_200_OK)


    def delete(self, request, user_pk):
        """ Deletes an specific user

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        user_pk: int
            Pk of specific user

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
        if not payload or not user:
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_401_MESSAGE
            }, status=status.HTTP_401_UNAUTHORIZED)

        if (
            isinstance(user, User) and
            (request.data["rol"] == ADMIN or user.pk != user_pk)
        ):
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_403_MESSAGE
            }, status=status.HTTP_403_FORBIDDEN)

        if isinstance(user, Root) and request.data["rol"] != ADMIN:
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_403_MESSAGE
            }, status=status.HTTP_403_FORBIDDEN)

        user_to_delete = User.objects.filter(pk=user_pk, rol=request.data["rol"]).first()
        if not user_to_delete:
            return Response({
                "code": "user_not_found",
                "detailed": "No existe un usuario con ese id"
            }, status=status.HTTP_404_NOT_FOUND)

        user_to_delete.delete()
        return Response({
            "deleted": user_to_delete.pk,
            "code": "user_deleted",
            "detailed": "Usuario eliminado correctamente"
        }, status=status.HTTP_200_OK)


class AdminApi(APIView, TokenHandler):
    """ Defines the http verbs to admin management """
    
    def post(self, request): 
        """ Creates a new Admin.

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
            "email": {"required": True, "type": "string"},
            "document_type": {
                "required": True, "type": "string",
                "allowed": [item[0] for item in _DOCUMENT_TYPE_CHOICES]
            },
            "document": {"required": True, "type": "string", "regex": r"^\d*$"},
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

        payload, user = self.get_payload(request)
        if not payload or not isinstance(user, Root):
            return Response({
                "code": "do_not_have_permission",
                "detailed": _STATUS_403_MESSAGE
            }, status=status.HTTP_403_FORBIDDEN)

        admin = User.objects.filter(
            Q(document=request.data["document"]) | Q(email=request.data["email"]))
        if admin:
            return Response({
                "code": "integrity_error",
                "detailed": "Ya existe un usuario registrado con ese documento o email"
            }, status=status.HTTP_409_CONFLICT)

        request.data["rol"] = ADMIN
        request.data["token"] = random.randint(0000, 9999)
        request.data["password"] = make_password(request.data["password"])

        admin = User.objects.create(**request.data)

        send_template_email(
            email_id=ADMIN_REGISTER_CONFIRMATION,
            params={
                "full_name": admin.get_full_name,
                "url": "" ## Acá lo tengo que mandar a una vista de front, donde pueda llenar los datos, con el token y el pk
            },
            receivers=admin.email,
            tracking_dict={
                "id_module": admin.pk,
                "type_module": ADMIN
            }
        )
        return Response({
            "inserted": admin.pk
        }, status=status.HTTP_201_CREATED)


class ConfirmRegisterApi(APIView, TokenHandler):
    """ Defines the http verbs to confirm register management """

    def patch(self, request, pk, token):
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
        validator = Validator({
            "is_admin": {"required": True, "type": "boolean"},
            "first_name": {
                "required": True, "type": "string", 
                "dependencies": {"is_admin": True}
            },
            "last_name": {
                "required": True, "type": "string", 
                "dependencies": {"is_admin": True}
            },
            "birth_date": {
                "required": True, "type": "string", 
                "regex": r"(19[2-9]\d|20[0-1]\d|2023)-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])",
                "dependencies": {"is_admin": True}
            },
            "email": {
                "required": True, "type": "string", 
                "dependencies": {"is_admin": True}
            },
            "address": {
                "required": True, "type": "string",
                "dependencies": {"is_admin": True}
            },
            "cellphone": {
                "required": True, "type": "string", 
                "minlength": 10, "dependencies": {"is_admin": True}
            },
            "gender": {
                "required": True, "type": "string",
                "allowed": [item[0] for item in _GENDER_CHOICES],
                "dependencies": {"is_admin": True}
            }
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": _STATUS_400_MESSAGE,
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(
            pk=pk, token=token, 
            rol=CLIENT if "is_admin" not in request.data else ADMIN
        )

        if not user:
            return Response({
                "code": "invalid_token",
                "detailed": "No existe un usuario con ese id y token"
            }, status=status.HTTP_400_BAD_REQUEST)

        if user.first().rol == ADMIN:
            request.data["status"] = APPROVED
            request.data["token"] = random.randint(0000, 9999)
            user.update(**request.data)
            return Response({
                "code": "admin_approved",
                "detailed": "Administrador aprobado correctamente"
            }, status=status.HTTP_200_OK)

        user.first().status = APPROVED
        user.first().token = random.randint(0000, 9999)
        user.first().save()
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
