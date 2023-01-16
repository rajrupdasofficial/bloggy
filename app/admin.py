from django.contrib import admin
from .models import Blog
# Register your models here.
#@admin.register(Blog)
#class PostAdmin(admin.ModelAdmin):
#    class Media:
#        js = ('static/js/uploader.js')


admin.site.register(Blog)
#admin.site.register(PostAdmin)