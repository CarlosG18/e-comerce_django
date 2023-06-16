# Generated by Django 4.2 on 2023-06-15 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0005_itemcarrinho_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcarrinho',
            name='preco_acumulado',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]