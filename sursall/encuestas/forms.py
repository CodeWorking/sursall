
from django import forms

class ContactoForm(forms.Form):
    correo = forms.EmailField(label='EMAIL:')
    mensaje = forms.CharField(widget = forms.Textarea)
    