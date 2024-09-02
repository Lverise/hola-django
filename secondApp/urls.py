from django.urls import path
from . import views

urlpatterns = [
    path('hola2/', views.hola2, name='hola2'),
]