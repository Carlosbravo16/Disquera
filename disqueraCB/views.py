from django.shortcuts import render
from django.http import HttpResponse
from .models import Disquera
from .models import Artista

# Create your views here.
def inicio(request):#vista1
    return HttpResponse("<h1>Bienvenido a la app </h1>")

def artista(request):#vista inicio artistas
    artistas=Artista.objects.all()
    return render(request, 'artistas/index.html',{'artistas':artistas})
def addartista(request):
    return render(request, 'artistas/crear.html')
def editarartista(request):
    return render(request, 'artistas/editar.html')

def genero(request):#vista inicio genero
    return render(request, 'generos/index.html')
def addgenero(request):
    return render(request, 'generos/crear.html')
def editargenero(request):
    return render(request, 'generos/editar.html')

def album(request):#vista inicio album
    return render(request, 'albunes/index.html')
def addalbum(request):
    return render(request, 'albunes/crear.html')
def editalbum(request):
    return render(request, 'albunes/editar.html')

def disquera(request):#Vista inicio disquera
    disqueras=Disquera.objects.all()
    return render(request, 'disqueras/index.html',{'disqueras':disqueras})
def adddisquera(request):
    return render(request, 'disqueras/crear.html')
def editdisquera(request):
    return render(request, 'disqueras/editar.html')

def cancion(request):#vista inicio cancion
    return render(request, 'canciones/index.html')
def addcancion(request):
    return render(request, 'canciones/crear.html')
def editcancion(request):
    return render(request, 'canciones/editar.html')