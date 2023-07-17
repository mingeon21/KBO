from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("status/", include("status.urls")),
    path('admin/', admin.site.urls),
]
