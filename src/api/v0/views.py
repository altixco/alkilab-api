from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from alkilab.apps.reservations.models import Room
from .serializers import RoomSerializer



class RoomViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    
    def list(self, request):

        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)