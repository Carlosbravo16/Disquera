from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):#vista1
    return HttpResponse("<h1>Bienvenido a la app </h1>")
def pagina1(request):
    return render(request, 'views/pagina1.html')

def artista(request):#vistainicio artistas
    return render(request, 'artistas/index.html')
def addartista(request):
    return render(request, 'artistas/crear.html')
def editarartista(request):
    return render(request, 'artistas/editar.html')

def genero(request):#vistainicio artistas
    return render(request, 'generos/index.html')
def addgenero(request):
    return render(request, 'generos/crear.html')
def editargenero(request):
    return render(request, 'generos/editar.html')