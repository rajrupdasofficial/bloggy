from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VideoUpload
from .serializers import VideoUploadSerializer
from rest_framework import permissions

# Create your views here.



class IndexAPIView(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request):
        all_videos = VideoUpload.objects.all().order_by('-created')
        serializer = VideoUploadSerializer(all_videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response({'error': 'Something went wrong. Please try again.'}, status=400)

