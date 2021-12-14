from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('temas/', views.mostrarCategorias, name='mostrar_categorias')
    
]