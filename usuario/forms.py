from django import forms

class UsuarioForm(forms.Form):
    numero_socio = forms.IntegerField()
    nombre = forms.CharField(max_length=30)