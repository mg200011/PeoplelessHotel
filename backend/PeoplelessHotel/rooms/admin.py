from django.contrib import admin

# Register your models here.
from .models import Rooms


class RoomsAdmin(admin.ModelAdmin):
    list_display = ['id','number','type','description','creation_date']
    search_fields = ('id','number','type','description','creation_date')
    pass
admin.site.register(Rooms, RoomsAdmin)