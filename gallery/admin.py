from django.contrib import admin
from .models import (Photo, PhotoDetails)

class PhotoAdmin(admin.StackedInline):
    model = Photo


@admin.register(PhotoDetails)
class PhotoDetailAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]


@admin.register(Photo)
class PhotoUploadAdmin(admin.ModelAdmin):
    list_per_page = 30
