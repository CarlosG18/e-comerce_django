# Generated by Django 4.2 on 2023-06-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0007_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='close_car',
            field=models.BooleanField(default=False),
        ),
    ]
