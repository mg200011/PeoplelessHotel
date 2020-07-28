from django.contrib import admin

# Register your models here.
from .models import Rooms


class RoomsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rooms, RoomsAdmin)