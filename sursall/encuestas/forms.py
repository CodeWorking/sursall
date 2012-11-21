from django import forms
from django.db import models
from encuestas.models import Pregunta

class ContactoForm(forms.Form):
    Nombre = forms.CharField()
    correo = forms.EmailField(label='Email:')
    mensaje = forms.CharField(widget = forms.Textarea)
    
class PreguntaForm(forms.Form):
    pregunta = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Pregunta.objects.all())
    respuestas = forms.ChoiceField(widget=forms.RadioSelect)
    def __init__(self, pregunta, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)
        self.fields['pregunta'].initial=pregunta.id
        respuestas = []
        for rs in pregunta.respuesta_set.all():
            respuestas.append((rs.id,"%s. %s" %(rs.orden_letra, rs.descripcion)))
        self.fields['respuestas'].choices = respuestas

class GestionResultados(forms.Form):
    pass