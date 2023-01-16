from django.urls import path
from .views import IndexView,BlogDetailView
urlpatterns = [
 path("",IndexView.as_view(),name="indexpage"),
 path("detail/<slug:slug>",BlogDetailView.as_view(),name="article-detail")
]
