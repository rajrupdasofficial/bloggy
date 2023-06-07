from django.urls import path
from account.views import Registration


app_name = 'account'

urlpatterns = [
    path('signup',Registration.as_view(),name='signup'),
]