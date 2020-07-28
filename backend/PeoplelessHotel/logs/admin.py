from django.contrib import admin

# Register your models here.
from .models import Logs


class LogsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Logs, LogsAdmin)