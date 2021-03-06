import base64
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.decorators import *
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

from PeoplelessHotel import settings
from reservations.models import Reservations

import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType


# Create your views here.
from PeoplelessHotel.custom_auth import CsrfExemptSessionAuthentication
from django.core.files.base import ContentFile


class GuestsService(ModelViewSet):
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    rest_serializer = GuestsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    @classmethod
    def convertb64(cls, image):
        format, imgstr = image.split(';base64,')
        ext = format.split('/')[-1]
        m = hashlib.md5()
        m.update(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode('utf-8'))
        image_data = ContentFile(b64decode(imgstr), name=m.hexdigest() + "." + ext)
        return image_data

    def create(self, request, *args, **kwargs):

        try:
            data = request.data

            result = super(GuestsService, self).create(request, *args, **kwargs)

            obj = Guests.objects.get(pk=result.data['id'])
            if "image1" in data:
                obj.image_sample_1 = self.convertb64(data['image1'])
            if "image2" in data:
                obj.image_sample_2 = self.convertb64(data['image2'])
            if "image3" in data:
                obj.image_sample_3 = self.convertb64(data['image3'])
            obj.save()
            obj = Guests.objects.get(pk=result.data['id'])

            result.data = GuestsSerializer(obj).data

            return result

        except Exception as E:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            data = request.data

            result = super(GuestsService, self).update(request, *args, **kwargs)

            obj = Guests.objects.get(pk=kwargs['pk'])
            if "image1" in data:
                obj.image_sample_1 = self.convertb64(data['image1'])
            if "image2" in data:
                obj.image_sample_2 = self.convertb64(data['image2'])
            if "image3" in data:
                obj.image_sample_3 = self.convertb64(data['image3'])
            obj.save()
            obj = Guests.objects.get(pk=kwargs['pk'])

            result.data = GuestsSerializer(obj).data

            return result

        except Exception as E:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    @api_view(['GET'])
    def create_person_group(request, reservation_id):

        try:
            # Create an authenticated FaceClient.
            face_client = FaceClient(settings.FACE_ENDPOINT, CognitiveServicesCredentials(settings.FACE_SUBSCRIPTION_KEY))

            '''
            Create person group:
                No parameters required
                Responds with a groupid
            '''

            # Used in the Person Group Operations,  Snapshot Operations, and Delete Person Group examples.
            # You can call list_person_groups to print a list of preexisting PersonGroups.
            # SOURCE_PERSON_GROUP_ID should be all lowercase and alphanumeric. For example, 'mygroupname' (dashes are OK).

            PERSON_GROUP_ID = str(uuid.uuid4())
            print('Person group:', PERSON_GROUP_ID)
            try:
                face_client.person_group.delete(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)
            except:
                print('failed to delete existing group')
            face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)

            # Store PERSON_GROUP_ID to given reservation
            Reservations.objects.filter(pk=int(reservation_id)).update(person_group_id=PERSON_GROUP_ID)

            return Response(PERSON_GROUP_ID, status=status.HTTP_201_CREATED)

        except Exception as E:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    @api_view(['GET'])
    def add_person_to_group(request, person_group_id, guest_id):
        try:
            # Create an authenticated FaceClient.
            face_client = FaceClient(settings.FACE_ENDPOINT, CognitiveServicesCredentials(settings.FACE_SUBSCRIPTION_KEY))

            '''
            Create a person and add a name to it
                Person id, and image list
            '''

            person = face_client.person_group_person.create(person_group_id, int(guest_id))

            Guests.objects.filter(pk=int(guest_id)).update(person_id=person.person_id)

            guest_record = Guests.objects.get(pk=int(guest_id))

            if guest_record.image_sample_1 is not None:
                w = open(guest_record.image_sample_1.path, 'r+b')
                face_client.person_group_person.add_face_from_stream(person_group_id, person.person_id, w)
            if guest_record.image_sample_2 is not None:
                w = open(guest_record.image_sample_2.path, 'r+b')
                face_client.person_group_person.add_face_from_stream(person_group_id, person.person_id, w)
            if guest_record.image_sample_3 is not None:
                w = open(guest_record.image_sample_3.path, 'r+b')
                face_client.person_group_person.add_face_from_stream(person_group_id, person.person_id, w)

            return Response(status=status.HTTP_200_OK)

        except Exception as E:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    @api_view(['GET'])
    def train_person_group(request, person_group_id):

        try:
            # Create an authenticated FaceClient.
            face_client = FaceClient(settings.FACE_ENDPOINT, CognitiveServicesCredentials(settings.FACE_SUBSCRIPTION_KEY))

            '''
            Train PersonGroup
                Only parameters should be persongroup. 
            '''

            print('Training the person group...')
            face_client.person_group.train(person_group_id)
            while True:
                training_status = face_client.person_group.get_training_status(person_group_id)
                print("Training status: {}.".format(training_status.status))
                print()
                if training_status.status is TrainingStatusType.succeeded:
                    break
                elif training_status.status is TrainingStatusType.failed:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                time.sleep(5)
            print("Training complete")

            return Response(status=status.HTTP_200_OK)

        except Exception as E:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    @csrf_exempt
    def identify_in_person_group(cls, request, room_id):

        try:
            # Create an authenticated FaceClient.
            face_client = FaceClient(settings.FACE_ENDPOINT, CognitiveServicesCredentials(settings.FACE_SUBSCRIPTION_KEY))


            '''
            Identify a face against a defined PersonGroup
                send groupid and images
            '''

            # GET person_group_id from RESERVATIONS - THE LAST CHECKED IN RESERVATION
            # Store PERSON_GROUP_ID to given reservation
            reservation_results = Reservations.objects.filter(rooms__room__id=int(room_id), status="CHECKED_IN")

            if len(reservation_results) > 0:

                data = JSONParser().parse(request)
                image = data['image']

                format, imgstr = image.split(';base64,')
                ext = format.split('/')[-1]
                m = hashlib.md5()
                m.update(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode('utf-8'))
                image_data = ContentFile(b64decode(imgstr), name=m.hexdigest() + "." + ext)

                # Group image for testing against
                group_photo = image_data.file

                face_ids = []
                faces = face_client.face.detect_with_stream(group_photo)
                for face in faces:
                    face_ids.append(face.face_id)

                if len(face_ids) > 0 :
                    # Identify faces
                    results = face_client.face.identify(face_ids, reservation_results[0].person_group_id)

                    if not results:
                        return HttpResponse({"result": "Access Denied!"}, status=406)
                    else:
                        tmp_guest = Guests.objects.filter(person_id=results[0].candidates[0].person_id)
                        if len(tmp_guest) > 0 and json.dumps(tmp_guest[0].rooms).__contains__(str(room_id)):
                            return HttpResponse({"result": "Success!", "data": GuestsSerializer(tmp_guest[0]).data}, status=200)
                        else:
                            return HttpResponse({"result": "Access Denied for that room!"}, status=406)
                else:
                    return HttpResponse({"result": "No faces detected!"}, status=406)
            else:
                return HttpResponse({"result": "Access Denied!"}, status=406)


            # for person in results:
            #     print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0].confidence))  # Get topmost confidence score

        except Exception as E:
            return HttpResponse({"result": "Access Denied!"}, status=400)

    @csrf_exempt
    @api_view(['GET'])
    def delete_person_group(request, person_group_id):

        try:
            # Create an authenticated FaceClient.
            face_client = FaceClient(settings.FACE_ENDPOINT, CognitiveServicesCredentials(settings.FACE_SUBSCRIPTION_KEY))

            '''
            Destroy the group with all info
                Only parameter: group-id
            '''

            face_client.person_group.delete(person_group_id)
            print("Deleted the person group {} from the target location.".format(person_group_id))

            return Response(status=status.HTTP_200_OK)

        except Exception as E:
            return Response(status=status.HTTP_400_BAD_REQUEST)
