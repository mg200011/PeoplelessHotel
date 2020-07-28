from django.contrib import admin

# Register your models here.
from .models import Loyalty_Program


class LoyaltyProgramAdmin(admin.ModelAdmin):
    pass
admin.site.register(Loyalty_Program, LoyaltyProgramAdmin)