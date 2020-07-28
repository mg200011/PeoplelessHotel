from rest_framework import serializers
from .models import *


class ReservationsRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations_Rooms
        fields = '__all__'