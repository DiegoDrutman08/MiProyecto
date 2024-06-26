# Generated by Django 5.0.4 on 2024-04-30 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0002_profesor_edad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='nombre',
            new_name='codigo',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos_vendedor', to='clase.vendedor'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos_cliente', to='clase.cliente'),
        ),
    ]
