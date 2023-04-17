from django.contrib import admin

from .models import Pelicula, ComentarioPelicula, Serie, ComentarioSerie

admin.site.register(Pelicula)
admin.site.register(ComentarioPelicula)
admin.site.register(Serie)
admin.site.register(ComentarioSerie)


# Register your models here.
