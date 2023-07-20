from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VideoUpload
from .serializers import VideoUploadSerializer,VideoPlayerSerializer
from rest_framework import permissions
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework_api_key.permissions import HasAPIKey

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class IndexAPIView(APIView):
    permission_classes = [HasAPIKey]

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request):
        all_videos = VideoUpload.objects.all().order_by('-created')
        serializer = VideoUploadSerializer(all_videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response({'error': 'Something went wrong. Please try again.'}, status=400)


class VideoDetailView(APIView):
    permission_classes = [HasAPIKey]

    @method_decorator(cache_page(CACHE_TTL))
    def post(request,vid):
        video_slug = get_object_or_404(VideoUpload, vid=vid)
        serializer = VideoPlayerSerializer(video_slug, many=True)
        return Response(serializer.data)
    
    def get(self, request):
        return Response({'error': 'Something went wrong. Please Try again'}, status=400)
