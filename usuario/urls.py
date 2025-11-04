from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
	path('registro/', views.registro),
	path('ingresar/',views.ingresar),
	path('salir/', LogoutView.as_view(), name='logout'),
	
]
