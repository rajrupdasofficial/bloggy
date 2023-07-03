from django.urls import path
from .views import IndexAPIView, VideoDetailView
app_name = "videoapp"
urlpatterns = [
    path('', IndexAPIView.as_view(), name="indexpage"),
    path('watch/v/<str:vid>',VideoDetailView.as_view(),name='detailvideo'),
]
