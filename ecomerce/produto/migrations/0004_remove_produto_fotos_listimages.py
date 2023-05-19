# Generated by Django 4.2.1 on 2023-05-17 17:15

from django.db import migrations, models
import django.db.models.deletion
import produto.models


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0003_alter_produto_fotos"),
    ]

    operations = [
        migrations.RemoveField(model_name="produto", name="fotos",),
        migrations.CreateModel(
            name="ListImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "foto",
                    models.ImageField(
                        default="produto/produto_default.png",
                        upload_to=produto.models.caminho_personalizado,
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="produto.produto",
                    ),
                ),
            ],
        ),
    ]