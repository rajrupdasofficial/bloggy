from django.contrib import admin
from .models import Blog,Analytics
# Register your models here.
@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ('title','created','updated',)
    list_display_links = ('title',)
    list_per_page = 30
@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_per_page=30