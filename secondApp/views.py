from django.shortcuts import render
from django.http import HttpResponse

def hola2(request):
    s ="<h1>Hola desde la app 2<h1/>"
    return HttpResponse(s)