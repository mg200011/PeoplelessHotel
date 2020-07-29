from django.contrib import admin

# Register your models here.
from .models import Reservations


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ['id','user','num_of_guests','checkin_date','num_of_days','status','creation_date']
    search_fields = ('id','user','num_of_guests','checkin_date','num_of_days','status','creation_date')
    pass
admin.site.register(Reservations, ReservationsAdmin)