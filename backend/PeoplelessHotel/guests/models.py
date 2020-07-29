from django.db import models

# Create your models here.
from reservations.models import Reservations
from rooms.models import Rooms
from base64 import b64decode
from django.core.files.base import ContentFile
import hashlib
from datetime import datetime
import datetime


class Guests(models.Model):
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE, related_name="guests_rooms")
    name = models.CharField(max_length=128, null=True, blank=True)
    rooms = models.CharField(max_length=256, null=True, blank=True)
    passport = models.CharField(max_length=64, null=True, blank=True)
    image_sample_1 = models.ImageField(upload_to='uploads/', null=True)
    image_sample_2 = models.ImageField(upload_to='uploads/', null=True)
    image_sample_3 = models.ImageField(upload_to='uploads/', null=True)

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"
