from django.db import models
from django.contrib.auth.models import User, Group, Permission

# Create your models here.


class Loyalty_Program(models.Model):
    user = models.ForeignKey(User, related_name="tasks_created", on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(null=False, blank=False)
    description = models.TextField()

    class Meta:
        verbose_name = "Loyalty Program"
        verbose_name_plural = "Loyalty Program"
