'''
Setup step
'''
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


# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
if os.environ.get('FACE_SUBSCRIPTION_KEY') is not None:
    KEY = os.environ['FACE_SUBSCRIPTION_KEY']
else:
    KEY = 'd018d09f705147bb8b4104faee1b2796'

# Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
# This endpoint will be used in all examples in this quickstart.
if os.environ.get('FACE_ENDPOINT') is not None:
    ENDPOINT = os.environ['FACE_ENDPOINT']
else:
    ENDPOINT = 'https://pampitafaceapi.cognitiveservices.azure.com/'

print(KEY + ' ' + ENDPOINT)
# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))







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





'''
Create a person and add a name to it
    Person id, and image list
'''
woman = face_client.person_group_person.create(PERSON_GROUP_ID, "Woman")
woman_images = [file for file in glob.glob('*.jpg') if file.startswith("woman")]
for image in woman_images:
    w = open(image, 'r+b')
    print("adding woman image")
    face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, woman.person_id, w)
'''
call it again
'''
man = face_client.person_group_person.create(PERSON_GROUP_ID, "Man")
man_images = [file for file in glob.glob('*.jpg') if file.startswith("man")]
for image in man_images:
    m = open(image, 'r+b')
    print("adding man image")
    face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, man.person_id, m)
'''
call it again
'''
child = face_client.person_group_person.create(PERSON_GROUP_ID, "Child")
child_images = [file for file in glob.glob('*.jpg') if file.startswith("child")]
for image in child_images:
    ch = open(image, 'r+b')
    print("adding child image")
    face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, child.person_id, ch)





'''
Train PersonGroup
    Only parameters should be persongroup. 
'''
print('Training the person group...')
face_client.person_group.train(PERSON_GROUP_ID)
while (True):
    training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
    print("Training status: {}.".format(training_status.status))
    print()
    if (training_status.status is TrainingStatusType.succeeded):
        break
    elif (training_status.status is TrainingStatusType.failed):
        sys.exit('Training the person group has failed.')
    time.sleep(5)
print("Training complete")





'''
Identify a face against a defined PersonGroup
    send groupid and images
'''
# Group image for testing against
group_photo = 'test-image-person-group.jpg'
IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))
# Get test image
test_image_array = glob.glob(os.path.join(IMAGES_FOLDER, group_photo))
image = open(test_image_array[0], 'r+b')
face_ids = []
faces = face_client.face.detect_with_stream(image)
for face in faces:
    face_ids.append(face.face_id)


# Identify faces
results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
print('Identifying faces in {}'.format(os.path.basename(image.name)))
if not results:
    print('No person identified in the person group for faces from {}.'.format(os.path.basename(image.name)))
for person in results:
    print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0].confidence)) # Get topmost confidence score





'''
Destroy the group with all info
    Only parameter: group-id
'''
face_client.person_group.delete(PERSON_GROUP_ID)
print("Deleted the person group {} from the target location.".format(PERSON_GROUP_ID))