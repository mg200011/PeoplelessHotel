from django.db import models
from enum import Enum


# Create your models here.
from reservations.models import Reservations
from rooms.models import Rooms


class ReservationRoomStatus(Enum):

    CHECKED_IN = "CHECKED_IN"
    CHECKED_OUT = "CHECKED_OUT"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Reservations_Rooms(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="reservations")
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE, related_name="rooms")
    num_of_guests = models.IntegerField(null=False, blank=False)
    checkin_date = models.DateField(null=True, blank=True)
    num_of_days = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=32, null=True, blank=True)