from django.contrib import admin
from .models import UserProfile
# Register your models here.

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','shortbio','created',)
    list_display_link = ('user',)
    list_per_page = 50