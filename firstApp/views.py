from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora Actual: </b>" +str(dt)
    return HttpResponse(s)

def formulario(request):
    hola ="<h1>Hola<h1/>"
    nombre = ["Usuario: ", "Pass: "]
    label=(f"<label>{nombre[0]}</label>")
    label2=(f"<label>{nombre[1]}</label>")
    input="<input></>"
    txt = (f"{hola+label+input+label2+input}")
    return HttpResponse(txt)