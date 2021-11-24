from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory
from sistema_venta.forms import BoletoForm

from sistema_venta.models import Funcion, Boleto

# Create your views here.
def detalle_funcion(request, id):
    # funcion = Funcion.objects.get(pk=id)
    funcion = get_object_or_404(Funcion, pk=id)
    return render(request, 'funciones/detalle.html', {'funcion':funcion})

def detalle_boleto(request, id):
    boleto = get_object_or_404(Boleto, pk=id)
    return render(request, 'boletos/detalle.html', {'boleto':boleto})


# BoletoForm = modelform_factory(Boleto)

def nuevo_boleto(request):
    if request.method == 'POST':
        formaBoleto = BoletoForm(request.POST)
        if formaBoleto.is_valid():
            formaBoleto.save()
            return redirect('index')
    else:
        formaBoleto = BoletoForm()

    return render(request, 'boletos/nuevo.html', {'formaBoleto':formaBoleto})
