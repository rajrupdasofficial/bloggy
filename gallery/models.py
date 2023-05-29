from django.db import models
import uuid
import os
from django.template.defaultfilters import slugify
import random
import string
from django.utils.crypto import get_random_string

# Create your models here.





def photo_upload_location(instance, image_name):
    url = instance.details.name
    image_name = f'{uuid.uuid5(uuid.NAMESPACE_URL,url).hex}.jpg'
    return os.path.join('gallery_images', image_name)


class PhotoDetails(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    upadate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"photo names are {self.name}"

    class Meta:
        verbose_name = 'Photo Detail'
        verbose_name_plural = 'Photo Details'


class Photo(models.Model):
    details = models.ForeignKey(PhotoDetails, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=photo_upload_location, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    upadate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"photo details are {self.details}"
