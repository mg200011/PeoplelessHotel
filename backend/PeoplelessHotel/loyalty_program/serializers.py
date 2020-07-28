from rest_framework import serializers
from .models import *


class LoyaltyProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loyalty_Program
        fields = '__all__'