from django.urls import path
from .views import admin_login_view

urlpatterns = [
    path('lz', admin_login_view, name="adminlogin"),
    # path('mz/', admindashboard, name="dashboard")
]
