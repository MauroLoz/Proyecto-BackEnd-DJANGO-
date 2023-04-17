from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pelicula, ComentarioPelicula, Serie, ComentarioSerie
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.db.models import Avg

from django.views.generic import TemplateView, ListView

from .forms import PeliculaForm
from .forms import SerieForm
# Create your views here.


def nuevapelicula(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST': 
                
                form = PeliculaForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()

                messages.success(request, 'Pelicula subida correctamente')
                return redirect('/')
            form = PeliculaForm()
            return render(request, 'nuevapelicula.html', {'form': form})
        else:
            return redirect('/')
    else:
        return render(request, 'sincuenta.html')
    

def nuevaserie(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST': 
                
                form = SerieForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()

                messages.success(request, 'Serie subida correctamente')
                return redirect('/')
            form = SerieForm()
            return render(request, 'nuevaserie.html', {'form': form})
        else:
            return redirect('/')
    else:
        return render(request, 'sincuenta.html')
    
    
def home(request): 
    if request.user.is_authenticated:
        peliculas = Pelicula.objects.order_by('-created')
        return render(request, 'inicio.html', {'peliculas':peliculas})
    else:
        return render(request, 'sincuenta.html')

def series(request): 
    if request.user.is_authenticated:
        series = Serie.objects.order_by('-created')
        return render(request, 'inicioserie.html', {'series':series})
    else:
        return render(request, 'sincuenta.html')

def comentario(request): 

    return render(request, 'comentario.html')


def pelicula(request):
    if request.user.is_authenticated:
        if request.method == 'POST': 
            Pelicula.objects.create(
                title = request.POST.get('title'),
                genero = request.POST.get('genero'),
                sinopsis = request.POST.get('sinopsis'),
                user = request.user
                )           
            messages.success(request, 'Pelicula subida correctamente')
            return redirect('/')
        return render(request, 'nuevapelicula.html')
    else:
        return render(request, 'sincuenta.html')


def verpelicula(request, id = None):
    if request.user.is_authenticated:
        if request.method == 'POST': 
            id = request.POST.get('id')
            p = Pelicula.objects.get(id = id)
            p.title = request.POST.get('title'),
            p.genero = request.POST.get('genero'),
            p.sinopsis = request.POST.get('sinopsis'),
            p.save()

        context = {}

        if id is not None:
            p = Pelicula.objects.get(id = id)
            context['pelicula'] = p
        

        c = ComentarioPelicula.objects.filter(post = id)

        vueltas = 0
        contador = 0
        for x in c:
            vueltas += 1
            contador += x.puntaje
            context['value'] = int(contador) / int(vueltas)


        return render(request, 'verpelicula.html', context)
    else:
        return render(request, 'sincuenta.html')


def verserie(request, id = None):
    if request.user.is_authenticated:
        if request.method == 'POST': 
            id = request.POST.get('id')
            p = Serie.objects.get(id = id)
            p.title = request.POST.get('title'),
            p.genero = request.POST.get('genero'),
            p.sinopsis = request.POST.get('sinopsis'),
            p.save()

        context = {}

        if id is not None:
            p = Serie.objects.get(id = id)
            context['serie'] = p

        c = ComentarioSerie.objects.filter(post = id)

        vueltas = 0
        contador = 0
        for x in c:
            vueltas += 1
            contador += x.puntaje
            context['value'] = int(contador) / int(vueltas)

        return render(request, 'verserie.html', context)
    else:
        return render(request, 'sincuenta.html')
    


def commentPelicula(request):
        if request.user.is_authenticated:
            p = Pelicula.objects.get(id = request.POST.get('pelicula'))
            ComentarioPelicula.objects.create(
            text = request.POST.get('text'),
            puntaje = request.POST.get('puntaje'),
            user = request.user,
            post = p
            )    
            return redirect('/')
        else:
            return render(request, 'sincuenta.html')

def commentSerie(request):
        if request.user.is_authenticated:
            p = Serie.objects.get(id = request.POST.get('serie'))
            ComentarioSerie.objects.create(
            text = request.POST.get('text'),
            puntaje = request.POST.get('puntaje'),
            user = request.user,
            post = p
            )    
            return redirect('/')
        else:
            return render(request, 'sincuenta.html')



def inicioSesion(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Se inicio Sesion correctamente')
                return redirect('/')
        messages.error(request, 'Datos incorrectos')

    return render(request, 'iniciosesion.html')


def registrar(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if(password != confirm_password):
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('/registro')

        User.objects.create_user(username, email=email, first_name=name, last_name=lastname, password=password)
        return redirect('/login/')
    return render(request, 'registrar.html')


def cierreSesion(request):
    logout(request)
    return redirect('/')


def perfil(request):
    
    if request.user.is_authenticated:
        comentario = ComentarioPelicula.objects.order_by('-created')
        return render(request, 'perfil.html', {'comentario':comentario})
    else:
        return render(request, 'sincuenta.html')
