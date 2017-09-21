from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from alkilab.apps.reservations.models import Room, Person

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializers import RoomSerializer, PersonSerializer, UserSerializer


class PersonViewSet(viewsets.ViewSet):

    def list(self, request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        people = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(people)
        return Response(serializer.data)

    def create(self, request):
        pass




class RoomViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    
    def list(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)