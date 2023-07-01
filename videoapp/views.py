from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VideoUpload
from .serializers import VideoUploadSerializer
from rest_framework import permissions
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class IndexAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request):
        all_videos = VideoUpload.objects.all().order_by('-created')
        serializer = VideoUploadSerializer(all_videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response({'error': 'Something went wrong. Please try again.'}, status=400)
