# Generated by Django 3.1.7 on 2021-06-30 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210628_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagenProducto',
            field=models.ImageField(default='sinfoto.jpg', upload_to='img/', verbose_name='Imagen del producto'),
        ),
    ]
