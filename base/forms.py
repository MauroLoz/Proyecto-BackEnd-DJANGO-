from django import forms
from .models import Pelicula, Serie

class PeliculaForm(forms.ModelForm):
   class Meta:
      model = Pelicula
      fields = '__all__'

class SerieForm(forms.ModelForm):
   class Meta:
      model = Serie
      fields = '__all__'