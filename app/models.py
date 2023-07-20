from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
import random
import string
from io import BytesIO
from PIL import Image as Img
from django.core.files.uploadedfile import InMemoryUploadedFile
from ckeditor_uploader.fields import RichTextUploadingField
import os
from django.conf import settings
import uuid


def random_string_generator(size=100, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Blog(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Blog", self.title, instance)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=255, default=None)
    thumbnail = models.ImageField(upload_to=image_upload_to, default=None)
    content = RichTextUploadingField()
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post name::  {self.title}"

    def save(self, *args, **kwargs):
        if self.thumbnail:
            img = Img.open(BytesIO(self.thumbnail.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((self.thumbnail.width / 1.5, self.thumbnail.height / 1.5), Img.ANTIALIAS)
            output = BytesIO()
            img.save(output, format='WebP', quality=70)
            output.seek(0)
            self.thumbnail = InMemoryUploadedFile(output, 'ImageField', "%s.webp" % self.thumbnail.name.join(
                random_string_generator()).split('.')[0:10], 'thumbnail/webp', len(output.getbuffer()), None)
        ud = str(uuid.uuid4())
        original_slug = slugify(self.title + '-' + ud)
        queryset = Blog.objects.all().filter(slug__iexact=original_slug).count()
        count = 1
        slug = original_slug
        while (queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Blog.objects.all().filter(slug__iexact=slug).count()
        self.slug = slug
        if self.featured:
            try:
                temp = Blog.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Blog.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})


class TestModel(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    ex = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"
