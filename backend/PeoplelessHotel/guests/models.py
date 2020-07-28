from django.db import models

# Create your models here.
from reservations.models import Reservations
from rooms.models import Rooms


class Guests(models.Model):
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE, related_name="guests_rooms")
    name = models.CharField(max_length=128, null=True, blank=True)
    passport = models.CharField(max_length=64, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image_sample_1 = models.ImageField(upload_to='uploads/')
    image_sample_2 = models.ImageField(upload_to='uploads/')
    image_sample_3 = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"
