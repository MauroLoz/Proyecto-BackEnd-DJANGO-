from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home),
    path('verseries', views.series),
    path('pelicula/', views.pelicula),
    path('pelicula/<int:id>', views.verpelicula),
    path('serie/<int:id>', views.verserie),
    path('commentPelicula/', views.commentPelicula),
    path('commentSerie/', views.commentSerie),
    path('login/', views.inicioSesion),
    path('logout/', views.cierreSesion),
    path('registro/', views.registrar),
    path('nuevapelicula/', views.nuevapelicula),
    path('nuevaserie/', views.nuevaserie),
    path('perfil/', views.perfil),
    path('recomendacion/', views.recomendacion),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)