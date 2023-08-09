from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('articulos/', articulos, name="articulos"),
    path('cursos/', cursos, name="cursos"),
    path('partners/', partners, name="partners"),
    path('ofertas/', ofertas, name="ofertas"),
    # rutas de los formularios
    path('articulos_form/', articulosForm, name="articulos_form"),
    path('cursos_form/', cursosForm, name="cursos_form"),
    path('partners_form/', partnersForm, name="partners_form"),
    path('ofertas_form/', ofertasForm, name="ofertas_form"),
    # rutas de busquedas
    path('buscar_comision/', buscarComision, name="buscar_comision"),
    path('buscar2/', buscar2, name="buscar2"),
]