# Generated by Django 4.2 on 2023-06-03 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('produto', '0001_initial'),
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcarrinho',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto'),
        ),
        migrations.AddField(
            model_name='carrinho',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.userpessoafisica'),
        ),
    ]
