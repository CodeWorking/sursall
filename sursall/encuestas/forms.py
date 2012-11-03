from django import forms
from django.db import models


class ContactoForm(forms.Form):
    Nombre = forms.CharField()
    correo = forms.EmailField(label='Email:')
    mensaje = forms.CharField(widget = forms.Textarea)
    
class PreguntaForm(forms.Form):
    Id = forms.CharField()