from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Pastikan baris ini ada
    path('api/', include('events.urls')),  # Pastikan path API aplikasi Anda
]
