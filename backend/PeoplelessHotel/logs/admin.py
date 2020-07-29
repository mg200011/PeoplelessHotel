from django.contrib import admin

# Register your models here.
from .models import Logs


class LogsAdmin(admin.ModelAdmin):
    list_display = ['id','creation_date','level','message']
    search_fields = ('id','creation_date','level','message')
    pass
admin.site.register(Logs, LogsAdmin)