from .views import *
from django.conf.urls import url
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)


# NOTE 1: [POST] /gusts/
# NOTE 2 : [POST] /guests/identify_in_person_group/<room_id>/    The type must be multipart and the name of the files must be 'image_sample_1', 'image_sample_2' and 'image_sample_3'


router.register(r'', GuestsService, basename="guests")

urlpatterns = router.urls

urlpatterns += [url(r'^create_person_group/(?P<reservation_id>[0-9]+)/$', GuestsService.create_person_group),]
urlpatterns += [url(r'^add_person_to_group/(?P<person_group_id>[0-9]+)/(?P<guest_id>[0-9]+)/$', GuestsService.add_person_to_group),]
urlpatterns += [url(r'^train_person_group/(?P<person_group_id>[0-9]+)/$', GuestsService.train_person_group),]
urlpatterns += [url(r'^identify_in_person_group/(?P<room_id>[0-9]+)/$', GuestsService.identify_in_person_group),]
urlpatterns += [url(r'^delete_person_group/(?P<person_group_id>[0-9]+)/$', GuestsService.delete_person_group),]