from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)
    idioma = models.CharField(max_length=255)
    estreno = models.DateField()
    duracion = models.DurationField()

    def __str__(self) -> str:
        return f'Pelicula {self.id}: {self.nombre}'


class Sala(models.Model):
    numero_sala = IntegerField()
    numero_asientos = IntegerField()
    capacidad = IntegerField()

    def __str__(self) -> str:
        return f'Sala {self.numero_sala}'


class Funcion(models.Model):
    hora = models.TimeField()
    dia = models.DateField()
    pelicula = ForeignKey(Pelicula, on_delete=models.SET_NULL, null=True)
    sala = ForeignKey(Sala, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'Funcion {self.id}: Hora->{self.hora}, Fecha->{self.dia}, {self.pelicula}, {self.sala}'


class Boleto(models.Model):
    funcion = ForeignKey(Funcion, on_delete=models.SET_NULL, null=True)
    numero_asiento = models.CharField(max_length=4)
    # numero_sala = models.IntegerField()
    precio = models.FloatField()

    def __str__(self) -> str:
        return f'Boleto {self.id}: {self.funcion}, Asiento: {self.numero_asiento}'
