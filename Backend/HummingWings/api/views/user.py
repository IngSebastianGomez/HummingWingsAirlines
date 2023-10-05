""" Contains User endpoint management definition """

from rest_framework import generics
from django.contrib.auth.hashers import make_password

from ..models.user import User
from ..serializers.userSerializer import UserSerializer


class UserApi(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
