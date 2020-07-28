from django.db import models
from enum import Enum


# Create your models here.

class ReservationStatus(Enum):

    RESERVED = "RESERVED"
    CANCELED = "CANCELED"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Reservations(models.Model):
    token = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(max_length=32, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)