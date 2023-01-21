from django.urls import path
from .views import index, blogdetail, galleryview, contactview, aboutview, watchview

urlpatterns = [
    path("", index, name="indexpage"),
    path("<slug:slug>.html", blogdetail, name="article-detail"),
    path("artgallery", galleryview, name="gallery"),
    path("contact", contactview, name="contact"),
    path("about", aboutview, name="about"),
    path("watch", watchview, name="videos"),
]
