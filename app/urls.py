from django.urls import path
from .views import index, blogdetail, galleryview

urlpatterns = [
    path("", index, name="indexpage"),
    path("<slug:slug>", blogdetail, name="article-detail"),
    path("artgallery", galleryview, name="gallery"),
]
