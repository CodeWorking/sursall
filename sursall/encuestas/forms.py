#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import Contacto, Comentario

class ContactoForm(forms.Form):
    correo = forms.EmailField(label='EMAIL:')
    mensaje = forms.CharField(widget = forms.Textarea)
