from django.urls import path
from . import views 

urlpatterns = [
    path('base', views.inicio,name='inicio'),
    
    path('artista',views.artista,name='artista'),
    path('artista/add',views.addartista,name='artista-add'),
    path('artista/edit',views.editarartista, name='artista-edit'),

    path('genero',views.genero,name='genero'),
    path('genero/add',views.addgenero,name='genero-add'),
    path('genero/edit',views.editargenero, name='genero-edit'), 

    path('album',views.album,name='album'),
    path('album/add',views.addalbum,name='album-add'),
    path('album/edit',views.editalbum,name='album-edit'),
]

