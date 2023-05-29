from django.contrib import admin
from .models import  VideoUpload,VideoFileDetails
# Register your models here.

class VideoAdmin(admin.StackedInline):
    model = VideoUpload
    exclude = ["slug",]


@admin.register(VideoFileDetails)
class VideoDetailsAdmin(admin.ModelAdmin):
    inlines = [VideoAdmin]
    list_display = ('name', 'created',)
    list_display_links = ('name',)
    list_per_page = 30


@admin.register(VideoUpload)
class VideoUploadAdmin(admin.ModelAdmin):
    exclude = ["slug",]
    list_per_page = 30
