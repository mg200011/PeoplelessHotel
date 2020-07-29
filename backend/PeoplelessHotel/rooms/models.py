from django.db import models

# Create your models here.
ROOM_TYPE = [
    ("SINGLE", "SINGLE"),
    ("DOUBLE", "DOUBLE"),
    ("DELUX", "DELUX"),
    ("PRESIDENTIAL", "PRESIDENTIAL")
]

class Rooms(models.Model):
    number = models.CharField(max_length=16, null=True, blank=True)
    type = models.CharField(max_length=128, choices=ROOM_TYPE)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return str(self.number) + '-' + str(self.type)
