# Generated by Django 4.2 on 2023-06-02 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField()),
                ('quantidade', models.IntegerField(default=0)),
                ('foto', models.ImageField(default='produto/produto_default.png', upload_to='produto/')),
                ('media_stars', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('status', models.CharField(choices=[('o', 'oferta'), ('f', 'falta'), ('n', 'normal')], default='n', help_text='status do produto', max_length=1)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ListImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(default='produto/produto_default.png', upload_to='produto/')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
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
