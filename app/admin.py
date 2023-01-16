from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ('title','created','updated',)
    list_display_links = ('title',)
    list_per_page = 30