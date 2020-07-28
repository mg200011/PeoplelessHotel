from django.contrib import admin

# Register your models here.
from .models import Guests


class GuestsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Guests, GuestsAdmin)