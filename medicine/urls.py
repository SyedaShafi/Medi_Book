
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', HomeView, name='home-view'),
    path('add/', AddMedicine, name='add-medicine'),
    path('get/<slug:slug>/', MedicineDescription, name='medicine-view'),
    path('edit/<slug:slug>/', edit_medicien, name='edit-view'),
    path('delete/<slug:slug>/', delete_medicien, name='delete-view'),
]
