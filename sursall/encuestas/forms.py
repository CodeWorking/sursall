from django import forms

class ContactoForm(forms.Form):
    Nombre = forms.CharField()
    correo = forms.EmailField(label='Email:')
    mensaje = forms.CharField(widget = forms.Textarea)
    