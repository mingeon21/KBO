from django.urls import path

from . import views

urlpatterns = [
    path("", views.loadfile, name="loadfile"),
    path('statistics/', views.result, name='result'), 
    path('ml/', views.ml, name='ml'), 
]

