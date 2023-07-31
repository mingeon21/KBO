from django.urls import path

from . import views

urlpatterns = [
    path("", views.loadfile, name="loadfile"),
    path('result/', views.result, name='result'), 
]

