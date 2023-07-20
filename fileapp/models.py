from django.db import models
# import uuid
import os
# from django.template.defaultfilters import slugify
# import random
# import string
# from django.utils.crypto import get_random_string

# Create your models here.


def file_upload_location(instance, filename):
    file_description = instance.details.name.lower().replace(" ", "-")
    file_name = filename.lower().replace(" ", "-")
    return os.path.join("New_files", file_description, file_name)


class FileDetail(models.Model):
    name = models.CharField(max_length=255, default=None)
    number_folder = models.CharField(max_length=255, default=None)
    created = models.DateTimeField(auto_now_add=True)
    upadate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"file name {self.name}"


class FileUpload(models.Model):
    details = models.ForeignKey(FileDetail, default=None, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_upload_location, null=True, blank=True)

    def __str__(self) -> str:
        return f"name of files uploaded are {self.file}"
