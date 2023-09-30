from rest_framework import generics
from ..models.user import User
from ..serializers.userSerializer import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
