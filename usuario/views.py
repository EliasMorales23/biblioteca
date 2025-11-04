from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def registro(request):
    return render(request, 'usuario/usuario.html')

def ingresar(request):
	return HttpResponse('ingresar')