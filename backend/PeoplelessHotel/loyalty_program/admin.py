from django.contrib import admin

# Register your models here.
from .models import Loyalty_Program


class LoyaltyProgramAdmin(admin.ModelAdmin):
    list_display = ['id','user','creation_date','points','description']
    search_fields = ('id','user','creation_date','points','description')
    pass
admin.site.register(Loyalty_Program, LoyaltyProgramAdmin)