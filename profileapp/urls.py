from django.urls import path
from .views import ProfileAPIView

app_name = 'profileapp'

urlpatterns = [
    path('profile',ProfileAPIView.as_view(),name="profile"),
]
