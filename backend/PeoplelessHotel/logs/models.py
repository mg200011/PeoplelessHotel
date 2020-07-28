from django.db import models

# Create your models here.


class Logs(models.Model):

    _DATABASE = "log"

    creation_date = models.DateTimeField()
    level = models.CharField(max_length=10)
    message = models.TextField()