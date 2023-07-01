from django.urls import path
from .views import IndexAPIView
app_name = "videoapp"
urlpatterns = [
    path('', IndexAPIView.as_view(), name="indexpage"),
]
