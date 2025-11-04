from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def registro(request):
	return HttpResponse('registro')

def ingresar(request):
	return HttpResponse('ingresar')