
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicine.urls')),
    path('auth/', include('accounts.urls')),
]
