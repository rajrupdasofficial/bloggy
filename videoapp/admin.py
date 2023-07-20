from django.contrib import admin
from .models import VideoUpload
# Register your models here.


@admin.register(VideoUpload)
class VideoUploadAdmin(admin.ModelAdmin):
    exclude = ["slug","vid"]
    list_per_page = 30
