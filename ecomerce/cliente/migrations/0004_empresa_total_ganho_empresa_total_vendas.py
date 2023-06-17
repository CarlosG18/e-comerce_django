# Generated by Django 4.2 on 2023-06-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_pessoafisica_total_compras_pessoafisica_total_gasto'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='total_ganho',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='empresa',
            name='total_vendas',
            field=models.IntegerField(default=0),
        ),
    ]
