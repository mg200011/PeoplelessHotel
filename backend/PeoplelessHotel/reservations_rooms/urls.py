from .views import *
from django.conf.urls import url
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'', ReservationsRoomsService, basename="reservationsrooms")

urlpatterns = router.urls