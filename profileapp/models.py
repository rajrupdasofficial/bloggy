from django.db import models
from django.conf import settings
# Create your models here.
import uuid
from io import BytesIO
from PIL import Image as Img
from django.core.files.uploadedfile import InMemoryUploadedFile
import random
import string
import os
from django.utils.crypto import get_random_string



def random_string_generator(size=100, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_gen(size=35):
    return ''.join(get_random_string(size))


def userprofile_image_upload_location(instance, imagename):
        rand_chars = get_random_string(20)
        image_file_area = rand_chars
        random_image_name = get_random_string(30)
        image_name = f"{random_image_name}_{imagename.lower().replace('-', '')}"
        return os.path.join(str(uuid.uuid4()), image_file_area, image_name)



class UserProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, related_name='author' , on_delete=models.CASCADE)
    profileimage = models.ImageField(upload_to=userprofile_image_upload_location,default=None, blank=True,null=True)
    shortbio=models.TextField(blank=True,null=True,default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    


