from django.contrib import admin
from .models import FileDetail, FileUpload
# Register your models here.


class FileAdmin(admin.StackedInline):
    model = FileUpload


@admin.register(FileDetail)
class DetailAdmin(admin.ModelAdmin):
    inlines = [FileAdmin]


@admin.register(FileUpload)
class UploadAdmin(admin.ModelAdmin):
    list_per_page = 30
