# Generated by Django 2.0.2 on 2023-05-10 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplos', '0028_auto_20230510_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleordencompra',
            name='precio_unitario',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
