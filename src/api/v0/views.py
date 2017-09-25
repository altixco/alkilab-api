from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.parsers import JSONParser

from alkilab.apps.reservations.models import Room, Person

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db import transaction, IntegrityError
from django.core.serializers import serialize

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

    @transaction.atomic
    def create(self, request):
        errors = []
        try:
            with transaction.atomic():
   
                data = request.data

                #save the user
                user_serializer = UserSerializer(data = data["user"]) 

                if not user_serializer.is_valid():
                    errors.append(user_serializer.errors)

                saved_user = user_serializer.save()
                data["user"] = saved_user.id

                #save the person
                person_serializer = PersonSerializer(data = data)

                if not person_serializer.is_valid():
                    errors.append(user_serializer.errors)
                
                person_serializer.save()

                return Response({'message': 'The resource has been created succesfuly'},status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({'message': 'InterityError'}, status=status.HTTP_409_CONFLICT)

        except:
            return Response({'message': errors },status=status.HTTP_409_CONFLICT)

        


class RoomViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    
    def list(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)