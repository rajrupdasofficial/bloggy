from django.contrib import admin
from .models import  VideoUpload,VideoFileDetails
# Register your models here.

@admin.register(VideoUpload)
class VideoUploadAdmin(admin.ModelAdmin):
    exclude = ["slug",]
    list_per_page = 30
