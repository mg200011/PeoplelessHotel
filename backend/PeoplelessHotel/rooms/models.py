from django.db import models

# Create your models here.


class Rooms(models.Model):
    number = models.CharField(max_length=16, null=True, blank=True)
    type = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    amenities = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
