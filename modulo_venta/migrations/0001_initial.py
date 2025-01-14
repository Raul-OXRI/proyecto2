# Generated by Django 5.0.6 on 2024-06-15 02:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulo_producto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='venta',
            fields=[
                ('venta_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField(auto_now_add=True)),
                ('total_venta', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='detalle_venta',
            fields=[
                ('detalle_venta_id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_producto.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_venta.venta')),
            ],
        ),
    ]
