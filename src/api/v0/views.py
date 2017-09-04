from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from alkilab.apps.reservations.models import Room, Person
from django.contrib.auth.models import User

from .serializers import RoomSerializer, PersonSerializer, UserSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class RoomViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    
    def list(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)