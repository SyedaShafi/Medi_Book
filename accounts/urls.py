
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/',login_view, name="login-view" ),
    path('logout/',logout_view, name="logout-view" ),
]
