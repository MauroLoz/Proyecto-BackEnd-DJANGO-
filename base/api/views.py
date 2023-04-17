from django.http import JsonResponse
from ..models import Pelicula, Serie, ComentarioPelicula, ComentarioSerie

def routes(request):
    routes = [
        'GET /api/peliculas',
        'GET /api/peliculas/:id'
        'GET /api/series',
        'GET /api/serie/:id'
    ]
    return JsonResponse(routes, safe=False)

def peliculas(request):
    peliculas = Pelicula.objects.all()
    posts_dict = []
    for p in peliculas:
        posts_dict.append({
            'title': p.title,
            'genero': p.genero,
            'sinopsis': p.sinopsis,
            'director': p.director,
            'nacionalidad': p.nacionalidad,
            'created': p.created,
            'id': p.id,
        })
    return JsonResponse(posts_dict, safe=False)

def pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    posts_dict = {
            'title': pelicula.title,
            'genero': pelicula.genero,
            'sinopsis': pelicula.sinopsis,
            'director': pelicula.director,
            'nacionalidad': pelicula.nacionalidad,
            'created': pelicula.created,
            'id': pelicula.id
    }
    return JsonResponse(posts_dict, safe=False)

def series(request):
    series = Serie.objects.all()
    posts_dict = []
    for s in series:
        posts_dict.append({
            'title': s.title,
            'genero': s.genero,
            'sinopsis': s.sinopsis,
            'temporadas': s.temporadas,
            'duracion': s.duracion,
            'created': s.created,
            'id': s.id,
        })
    return JsonResponse(posts_dict, safe=False)

def serie(request, id):
    serie = Serie.objects.get(id=id)
    posts_dict = {
            'title': serie.title,
            'genero': serie.genero,
            'sinopsis': serie.sinopsis,
            'temporadas': serie.temporadas,
            'duracion': serie.duracion,
            'created': serie.created,
            'id': serie.id
    }
    return JsonResponse(posts_dict, safe=False)


def comentarios(request):
    comentariosPeliculas = ComentarioPelicula.objects.all()
    comentariosSeries = ComentarioSerie.objects.all()
    posts_dict = []
    for cp in comentariosPeliculas:
        posts_dict.append({
            'test': cp.text,
            'puntaje': cp.puntaje,
            'id': cp.id,
        })
    for cs in comentariosSeries:
        posts_dict.append({
            'test': cs.text,
            'puntaje': cs.puntaje,
            'id': cs.id,
        })
    return JsonResponse(posts_dict, safe=False)