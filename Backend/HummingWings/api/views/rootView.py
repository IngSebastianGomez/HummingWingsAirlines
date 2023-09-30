# appHummingWings/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.root import Root
from ..serializers.rootSerializer import RootSerializer

class RootListCreateView(APIView):
    def get(self, request):
        roots = Root.objects.all()
        serializer = RootSerializer(roots, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RootSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
