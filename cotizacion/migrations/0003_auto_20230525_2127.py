# Generated by Django 3.2.19 on 2023-05-26 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0002_itemc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='productos',
        ),
    ]
