# Generated by Django 4.2.1 on 2023-05-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0002_produto_fotos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="fotos",
            field=models.ImageField(
                default="produto/produto_default.png", upload_to="produto/"
            ),
        ),
    ]