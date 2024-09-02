from django.urls import path
from . import views

urlpatterns = [
    path('', views.display),
    path('datetime/', views.displayDateTime, name='display_datetime'),
    path('formulario/', views.formulario, name='formulario'),
]
