from django.db import models

# Create your models here.
from reservations.models import Reservations
from rooms.models import Rooms
from base64 import b64decode
from django.core.files.base import ContentFile
import hashlib
from datetime import datetime
import datetime



class Image(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='uploads/', null=True)


    @classmethod
    def get_path(cls):
        return "static/" + cls.path

    @classmethod
    def create(cls, **args):
        aux=cls(**args)
        aux.save()
        return aux

    @classmethod
    def convertb64(cls, image):
        format, imgstr = image.split(';base64,')
        ext = format.split('/')[-1]
        m = hashlib.md5()
        m.update(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode('utf-8'))
        image_data = ContentFile(b64decode(imgstr), name=m.hexdigest() + "." + ext)
        return image_data

    @classmethod
    def createb64(cls, image):
        format, imgstr = image.split(';base64,')
        ext = format.split('/')[-1]
        m = hashlib.md5()
        m.update(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode('utf-8'))
        image_data = ContentFile(b64decode(imgstr), name=m.hexdigest() + "." + ext)
        aux = cls.create(file=image_data)
        return aux

    @classmethod
    def createWithImage(cls, image, ext):
        m = hashlib.md5()
        m.update(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode('utf-8'))
        image_data = ContentFile(image, name=m.hexdigest() + "." + ext)
        aux = cls.create(file=image_data)
        return aux

class Guests(models.Model):
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE, related_name="guests_rooms")
    name = models.CharField(max_length=128, null=True, blank=True)
    passport = models.CharField(max_length=64, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image_sample_1 = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE, related_name='%(class)s_img1')
    image_sample_2 = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE, related_name='%(class)s_img2')
    image_sample_3 = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE, related_name='%(class)s_img3')

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"
