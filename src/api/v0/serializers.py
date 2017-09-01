from rest_framework import serializers
from alkilab.apps.reservations.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')
