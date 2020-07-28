from django.contrib import admin

# Register your models here.
from .models import Reservations


class ReservationsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reservations, ReservationsAdmin)