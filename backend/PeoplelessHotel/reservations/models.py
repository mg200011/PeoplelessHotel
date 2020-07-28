from django.db import models
from enum import Enum


# Create your models here.

class ReservationStatus(Enum):

    RESERVED = "RESERVED"
    CANCELED = "CANCELED"
    CHECKED_IN = "CHECKED_IN"
    CHECKED_OUT = "CHECKED_OUT"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Reservations(models.Model):
    num_of_guests = models.IntegerField(null=False, blank=False)
    checkin_date = models.DateField(null=True, blank=True)
    num_of_days = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=32, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
