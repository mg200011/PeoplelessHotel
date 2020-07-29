from django.db import models
from enum import Enum


# Create your models here.
from reservations.models import Reservations
from rooms.models import Rooms


class Reservations_Rooms(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="reservations")
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE, related_name="rooms")

    class Meta:
        verbose_name = "Reservations Rooms"
        verbose_name_plural = "Reservations Rooms"

    def __str__(self):
        return str(self.reservation) + '-' + str(self.room)