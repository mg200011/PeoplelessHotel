from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import *
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

# Create your views here.


class LoyaltyProgramService(ModelViewSet):
    queryset = Loyalty_Program.objects.all()
    serializer_class = LoyaltyProgramSerializer
    rest_serializer = LoyaltyProgramSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)