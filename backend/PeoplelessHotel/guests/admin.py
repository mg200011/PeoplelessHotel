from django.contrib import admin

# Register your models here.
from .models import Guests


class GuestsAdmin(admin.ModelAdmin):
    list_display = ['id','name','passport','birthdate']
    search_fields = ('id','name','passport','birthdate')
    pass
admin.site.register(Guests, GuestsAdmin)
