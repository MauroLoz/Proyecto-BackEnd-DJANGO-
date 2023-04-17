from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


# Create your models here.


class Pelicula(models.Model):
    title=models.CharField(max_length=100)
    genero_box=(
        ('Accion', 'Accion'),
        ('Terror', 'Terror'),
        ('Drama', 'Drama'),
        ('Documental', 'Documental'),
        ('Comedia', 'Comedia'),
        ('Romantica', 'Romantica'),
        ('Ciencia Ficcion', 'Ciencia Ficcion'),
        ('Animada', 'Animada'),
    )
    genero = models.CharField(max_length=15, choices=genero_box)
    sinopsis = models.TextField()
    director = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=200)
    image = models.ImageField(upload_to='base/Images/moviesPIC')
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    def avg_ratings(self):
        return self.comments.aggregate(
            Avg('puntaje')
        )

class Serie(models.Model):
    title=models.CharField(max_length=100)
    genero_box=(
        ('Accion', 'Accion'),
        ('Terror', 'Terror'),
        ('Drama', 'Drama'),
        ('Documental', 'Documental'),
        ('Comedia', 'Comedia'),
        ('Romantica', 'Romantica'),
        ('Ciencia Ficcion', 'Ciencia Ficcion'),
        ('Animada', 'Animada'),
    )
    genero = models.CharField(max_length=15, choices=genero_box)
    sinopsis = models.TextField()
    temporadas = models.IntegerField()
    duracion = models.IntegerField()
    image = models.ImageField(upload_to='base/Images/seriesPIC')
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title


class ComentarioPelicula(models.Model):
    puntaje_box=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    puntaje = models.IntegerField(choices=puntaje_box)
    text = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    post = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class ComentarioSerie(models.Model):
    puntaje_box=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    puntaje = models.IntegerField(choices=puntaje_box)
    text = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    post = models.ForeignKey(Serie, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)