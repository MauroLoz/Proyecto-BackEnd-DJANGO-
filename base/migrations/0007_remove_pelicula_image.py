# Generated by Django 4.1.7 on 2023-04-01 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_pelicula_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='image',
        ),
    ]