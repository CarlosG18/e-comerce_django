# Generated by Django 4.2 on 2023-05-30 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_cliente_type_cliente'),
        ('produto', '0009_produto_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='media_stars',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='listimages',
            name='foto',
            field=models.ImageField(default='produto/produto_default.png', upload_to='produto/'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('stars', models.IntegerField(choices=[(1, 'péssimo'), (2, 'mediano'), (3, 'ótimo'), (4, 'excelente'), (5, 'fantástico')])),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]
