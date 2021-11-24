from django.contrib import admin

from sistema_venta.models import Funcion, Pelicula, Sala, Boleto

# Register your models here.
admin.site.register(Funcion)
admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Boleto)
