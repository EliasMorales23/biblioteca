from django import forms

class LibroForm(forms.Form):
    isbn = forms.IntegerField()
    autor = forms.CharField()
    titulo = forms.CharField(max_length=30)
    estado = forms.BooleanField()