# Generated by Django 2.0.2 on 2023-05-10 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplos', '0029_detalleordencompra_precio_unitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleordencompra',
            name='orden_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='ejemplos.OrdenCompra'),
        ),
        migrations.AlterField(
            model_name='detalleordencompra',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
