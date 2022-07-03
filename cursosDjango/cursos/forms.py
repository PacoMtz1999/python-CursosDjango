from django import forms
from django.forms import fields
from .models import MensajeUsuario
from .models import Cursos

class MensajeUsuarioForm(forms.ModelForm):
    class Meta:
        model = MensajeUsuario
        fields = ['nombre', 'email', 'curso', 'telefono', 'mensaje']

class registroCurso(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre','mensaje']