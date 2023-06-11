from django.db import models
from django.conf import settings
# Create your models here.
import uuid
from io import BytesIO
from PIL import Image as Img
from django.core.files.uploadedfile import InMemoryUploadedFile
import random
import string
piuf = uuid.uuid4()

def random_string_generator(size=100, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def random_uuid():
    return uuid.uuid4()

class UserProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, related_name='author' , on_delete=models.CASCADE)
    profileimage = models.ImageField(upload_to=random_uuid(),default=None, blank=True,null=True)
    shortbio=models.TextField(blank=True,null=True,default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.profileimage:
            img = Img.open(BytesIO(self.profileimage.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((self.profileimage.width / 1.5, self.profileimage.height / 1.5), Img.ANTIALIAS)
            output = BytesIO()
            img.save(output, format='WebP', quality=60)
            output.seek(0)
            self.thumbnail = InMemoryUploadedFile(output, 'ImageField', "%s.webp" % self.profileimage.name.join(
                random_string_generator()).split('.')[0:10], 'profileimage/webp', len(output.getbuffer()), None)
        super().save(*args, **kwargs)
