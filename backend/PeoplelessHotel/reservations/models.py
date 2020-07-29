from django.db import models
from enum import Enum
from django.contrib.auth.models import User


# Create your models here.
RESERVATION_STATUS = [
    ("RESERVED", "RESERVED"),
    ("CANCELED", "CANCELED"),
    ("CHECKED_IN", "CHECKED_IN"),
    ("CHECKED_OUT", "CHECKED_OUT")
]

class Reservations(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    num_of_guests = models.IntegerField(null=False, blank=False)
    checkin_date = models.DateField(null=True, blank=True)
    num_of_days = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=32, choices=RESERVATION_STATUS, default='RESERVED')
    creation_date = models.DateTimeField(auto_now_add=True)
    person_group_id = models.CharField(max_length=64, null=True, blank=True )

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return str(self.id) + '-' + str(self.user)
