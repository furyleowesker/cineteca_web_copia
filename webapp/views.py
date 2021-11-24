from django.http.response import HttpResponse
from django.shortcuts import render

from sistema_venta.models import Funcion, Boleto

# Create your views here.
def bienvenido(request):
    numero_funciones = Funcion.objects.count()
    funciones = Funcion.objects.order_by('id')
    numero_boletos = Boleto.objects.count()
    boletos = Boleto.objects.order_by('id')
    return  render(request, 'bienvenido.html', {'numero_funciones':numero_funciones, 'funciones':funciones, 'numero_boletos':numero_boletos, 'boletos':boletos})
