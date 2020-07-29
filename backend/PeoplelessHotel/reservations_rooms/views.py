from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.decorators import *
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

# Create your views here.
from PeoplelessHotel.custom_auth import CsrfExemptSessionAuthentication


class ReservationsRoomsService(ModelViewSet):
    queryset = Reservations_Rooms.objects.all()
    serializer_class = ReservationsRoomsSerializer
    rest_serializer = ReservationsRoomsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)