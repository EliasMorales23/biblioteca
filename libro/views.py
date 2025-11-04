from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UsuarioForm
from .models import Usuario
# Create your views here.

def registro_libro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            numero_socio= form.cleaned_data['numero_socio']
            nombre = form.cleaned_data['nombre']
            Usuario.objects.create(
                numero_socio=numero_socio,
                nombre=nombre
            )

            # procesar o guardar el dato
    else:
        form = UsuarioForm()
    return render(request, 'usuario/usuario.html', {'form': form})
