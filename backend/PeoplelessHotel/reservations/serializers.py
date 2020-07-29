from rest_framework import serializers
from .models import *
from guests.serializers import GuestsSerializer
from reservations_rooms.serializers import ReservationsRoomsSerializer


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'


class ReservationsSerializerWithChilds(serializers.ModelSerializer):

    guests_rooms = GuestsSerializer(many=True, required=False)
    rooms = ReservationsRoomsSerializer(many=True, required=False)

    class Meta:
        model = Reservations
        fields = '__all__'
        fields = ('id', 'user', 'num_of_guests', 'checkin_date', 'num_of_days', 'status', 'creation_date', 'guests_rooms', 'rooms')