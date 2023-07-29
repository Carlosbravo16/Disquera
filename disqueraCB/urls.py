from django.urls import path
from . import views 
from django.conf import settings
from django.contrib.staticfiles.urls import static

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

    
    path('disquera', views.disquera, name='disquera'),
    path('disquera/add', views.adddisquera, name='disquera-add'),
    path('disquera/edit', views.editdisquera, name='disquera-edit'),

    path('views/canciones', views.cancion, name='cancion'),
    path('canciones/add', views.addcancion, name='cancion-add'),
    path('canciones/edit', views.editcancion, name='cancion-edit'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

