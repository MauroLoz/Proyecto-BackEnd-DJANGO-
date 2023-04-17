# Generated by Django 4.1.7 on 2023-04-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_pelicula_director_alter_pelicula_nacionalidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='puntaje',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.CharField(choices=[('Accion', 'Accion'), ('Terror', 'Terror'), ('Drama', 'Drama'), ('Documental', 'Documental'), ('Comedia', 'Comedia'), ('Romantica', 'Romantica'), ('Ciencia Ficcion', 'Ciencia Ficcion'), ('Animada', 'Animada')], max_length=15),
        ),
        migrations.AlterField(
            model_name='serie',
            name='genero',
            field=models.CharField(choices=[('Accion', 'Accion'), ('Terror', 'Terror'), ('Drama', 'Drama'), ('Documental', 'Documental'), ('Comedia', 'Comedia'), ('Romantica', 'Romantica'), ('Ciencia Ficcion', 'Ciencia Ficcion'), ('Animada', 'Animada')], max_length=15),
        ),
    ]
