# Generated by Django 3.2.9 on 2021-11-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_venta', '0002_auto_20211115_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcion',
            name='dia',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='funcion',
            name='hora',
            field=models.TimeField(),
        ),
    ]