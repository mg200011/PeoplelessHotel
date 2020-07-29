import json

from django.shortcuts import render

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


class GuestsService(ModelViewSet):
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    rest_serializer = GuestsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


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
            Reservations.objects.filter(pk=reservation_id).update(person_group_id=PERSON_GROUP_ID)

            return Response(PERSON_GROUP_ID, status=status.HTTP_201_CREATED)

        except Exception as E:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET'])
    def add_person_to_group(request, person_group_id, guest_id):
        try:
            # Create an authenticated FaceClient.
            face_client = FaceClient(settings.FACE_ENDPOINT, CognitiveServicesCredentials(settings.FACE_SUBSCRIPTION_KEY))

            '''
            Create a person and add a name to it
                Person id, and image list
            '''

            person = face_client.person_group_person.create(person_group_id, guest_id)

            guest_record = reservations = Guests.objects.get(pk=guest_id)

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


    @api_view(['POST']) #multipart 'image' file
    def identify_in_person_group(request, room_id):

        try:
            # Create an authenticated FaceClient.
            face_client = FaceClient(settings.FACE_ENDPOINT, CognitiveServicesCredentials(settings.FACE_SUBSCRIPTION_KEY))


            '''
            Identify a face against a defined PersonGroup
                send groupid and images
            '''

            # GET person_group_id from RESERVATIONS - THE LAST CHECKED IN RESERVATION
            # Store PERSON_GROUP_ID to given reservation
            reservation_results = Reservations.objects.filter(rooms__room__id=room_id, status="CHECKED_IN")

            if reservation_results:

                # Group image for testing against
                group_photo = request.FILES['image'].file

                face_ids = []
                faces = face_client.face.detect_with_stream(group_photo)
                for face in faces:
                    face_ids.append(face.face_id)

                # Identify faces
                results = face_client.face.identify(face_ids, reservation_results[0].person_group_id)

                if not results:
                    return Response(json.dumps({'message': 'Do not open the door'}), status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response(json.dumps({'message': 'Open the door'}), status=status.HTTP_302_FOUND)
            else:
                return Response(json.dumps({'message': 'Do not open the door'}), status=status.HTTP_404_NOT_FOUND)


            # for person in results:
            #     print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0].confidence))  # Get topmost confidence score

        except Exception as E:
            return Response(status=status.HTTP_400_BAD_REQUEST)



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
