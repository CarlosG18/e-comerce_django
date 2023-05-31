# Generated by Django 4.2 on 2023-05-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_cliente_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='type_cliente',
            field=models.CharField(choices=[('f', 'pessoa fisica'), ('e', 'empresa')], default='f', help_text='tipo de cliente', max_length=1),
        ),
    ]