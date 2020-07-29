from django.contrib import admin

# Register your models here.
from .models import Guests


class GuestsAdmin(admin.ModelAdmin):
    list_display = ['id','name','passport']
    search_fields = ('id','name','passport')
    pass
admin.site.register(Guests, GuestsAdmin)
