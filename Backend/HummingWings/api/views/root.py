""" Contains root user management definition """

from cerberus import Validator
from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..helpers.token import TokenHandler

from ..models.constants import _STATUS_400_MESSAGE, _STATUS_403_MESSAGE
from ..models.root import Root


class RootApi(APIView, TokenHandler):
    """ Contains root user management definition """

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
            "username": {"required": True, "type": "string"},
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

        root = Root.objects.filter(username=request.data["username"])
        if root:
            return Response({
                "code": "integrity_error",
                "detailed": "Ya existe un usuario registrado con ese nombre de usuario"
            }, status=status.HTTP_409_CONFLICT)

        request.data["password"] = make_password(request.data["password"])

        root = Root.objects.create(**request.data)

        return Response({
            "inserted": root.pk
        }, status=status.HTTP_201_CREATED)
