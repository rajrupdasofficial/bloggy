from django.urls import path
from account.views import Registration,Login


app_name = 'account'

urlpatterns = [
    path('signup',Registration.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
]