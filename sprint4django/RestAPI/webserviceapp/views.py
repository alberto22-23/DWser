from django.shortcuts import render
from django.http import HttpResponse

def pagina_de_prueba(request):
	return HttpResponse("<h1>Página de prueba</h1>");

# Create your views here.
