# Generated by Django 3.2.9 on 2021-11-15 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_venta', '0003_auto_20211115_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('idioma', models.CharField(max_length=255)),
                ('estreno', models.DateField()),
                ('duracion', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_sala', models.IntegerField()),
                ('numero_asientos', models.IntegerField()),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='funcion',
            name='pelicula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_venta.pelicula'),
        ),
        migrations.AlterField(
            model_name='funcion',
            name='sala',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_venta.sala'),
        ),
    ]
