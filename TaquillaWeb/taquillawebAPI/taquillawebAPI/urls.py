"""taquillawebAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from taquillawebapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', views.pagina_de_prueba),
    path('users/', views.nuevousuario_view),
    path('sessions/', views.login_view),
    path('cines/', views.cines_view),
    path('peliculas/', views.peliculas_view),
    path('peliculas/<int:id_solicitado>/', views.pelicula_por_id_view),
    path('cine/<int:id_cine_solicitado>/peliculas/', views.peliculas_por_cine_view),
    path('peliculas/estrenos/', views.peliculas_estrenos_view),
    path('entradas/', views.pedir_entradas_view),
    path('admin_austin_aforos/', views.cambio_aforos_austin),
    path('admin_borrado_entradas/', views.borrado_registros_tentradas),
    path('entradas/cine/<int:id_cine_solicitado>/', views.audiencia_peliculas_cine),
    path('buscar_pelicula/<str:cadena_solicitada>/', views.buscar_pelicula_view)
]