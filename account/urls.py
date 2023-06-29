from django.urls import path
from account.views import Registration,Login,Logout

app_name = 'account'

urlpatterns = [
    path('signup',Registration.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
]
