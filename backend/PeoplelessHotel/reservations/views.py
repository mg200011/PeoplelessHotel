from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import *
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

# Create your views here.


class ReservationsService(ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    rest_serializer = ReservationsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

    def get_queryset(self):
        queryset = Reservations.objects.all()

        if not self.request.user.is_superuser and not self.request.user.is_staff:
            queryset = queryset.filter(user_id=self.request.user.id)

        return queryset

    @api_view(['GET'])
    def get_user_reservations(request):

        try:
            reservations = Reservations.objects.filter(user_id=request.user.id)
            if reservations:
                serializer = ReservationsSerializerWithChilds(reservations, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)

        except Reservations.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET'])
    def get_user_reservation_by_id(request, reservation_id):

        try:
            reservations = Reservations.objects.filter(pk=reservation_id, user_id=request.user.id)
            if reservations:
                serializer = ReservationsSerializerWithChilds(reservations, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)

        except Reservations.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)

