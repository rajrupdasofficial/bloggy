from django.urls import path
from .views import IndexView,BlogDetailView,GalleryView,index
urlpatterns = [
 path("",index,name="indexpage"),
 path("<slug:slug>/",BlogDetailView.as_view(),name="article-detail"),
 path("m",GalleryView.as_view(),name="gallery")
]
