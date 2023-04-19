from django import forms
from .models import Pelicula, Serie, Recomendacion

class PeliculaForm(forms.ModelForm):
   class Meta:
      model = Pelicula
      fields = '__all__'

class SerieForm(forms.ModelForm):
   class Meta:
      model = Serie
      fields = '__all__'


class Recomendacion(forms.ModelForm):
   class Meta:
      model = Recomendacion
      fields = '__all__'