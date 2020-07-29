from .views import *
from django.conf.urls import url
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'', ReservationsService, basename="reservations")

urlpatterns = router.urls

urlpatterns += [url(r'^get_user_reservations/$', ReservationsService.get_user_reservations),]
urlpatterns += [url(r'^get_user_reservation_by_id/(?P<reservation_id>[0-9]+)/$', ReservationsService.get_user_reservation_by_id),]
