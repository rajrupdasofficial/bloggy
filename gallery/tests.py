from django.db import models
import base64
from rest_framework import serializers
from .models import UserProfile
class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    base64_image = models.TextField(null=True, blank=True)


def upload_profile_picture(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            # Read the image file
            image_data = profile_picture.read()
            # Encode the image data to base64 string
            base64_image = base64.b64encode(image_data).decode('utf-8')
            # Save the uploaded image and base64 string to the database
            user_profile = UserProfile(username=request.user.username, profile_picture=profile_picture, base64_image=base64_image)
            user_profile.save()

# <img src="data:image/png;base64,{{ user_profile.base64_image }}" alt="{{ user_profile.username }} profile picture">
import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UserProfile
# from .serializers import UserProfileSerializer

class UploadProfilePicture(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        profile_picture = request.data.get('profile_picture')
        if profile_picture:
            # Read the image file
            image_data = profile_picture.read()
            # Encode the image data to base64 string
            base64_image = base64.b64encode(image_data).decode('utf-8')
            # Save the uploaded image and base64 string to the database
            user_profile = UserProfile(username=request.user.username, profile_picture=profile_picture, base64_image=base64_image)
            user_profile.save()
            # Serialize the UserProfile instance and return the response
            
            # serializer = UserProfileSerializer(user_profile)
            # return Response(serializer.data)
        else:
            return Response({'error': 'No profile picture was uploaded'}, status=400)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'profile_picture', 'base64_image')
