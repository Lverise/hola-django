from firstApp import views as app1
from secondApp import views as app2
#import path, include


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de firstApp usando include
    path('firstApp/', include('firstApp.urls')),  # Mantén esto si tienes urls.py en firstApp

    # Rutas directas de firstApp
    path('hola/', app1.display),
    path('ahora/', app1.displayDateTime),
    path('formulario/', app1.formulario),

    path('secondApp/', include('secondApp.urls')),
    # Ruta directa de secondApp
    path('hola2/', app2.hola2),
]
#donde va hola/ es la ruta exacta que tendrá que
#escribir el usuario para entrar a la página