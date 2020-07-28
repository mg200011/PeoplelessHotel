from django.contrib import admin

# Register your models here.
from .models import Reservations_Rooms


class ReservationsRoomsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reservations_Rooms, ReservationsRoomsAdmin)