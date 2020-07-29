from rest_framework import serializers
from .models import *
from rooms.serializers import RoomsSerializer


class ReservationsRoomsSerializer(serializers.ModelSerializer):

    room = RoomsSerializer(many=False, required=False)

    class Meta:
        model = Reservations_Rooms
        fields = '__all__'