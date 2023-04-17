from django.urls import path
from . import views 

urlpatterns = [
     path('', views.routes),
     path('peliculas/', views.peliculas),
     path('peliculas/<int:id>', views.pelicula),
     path('series/', views.series),
     path('series/<int:id>', views.serie),
     path('comentarios/', views.comentarios),
]

