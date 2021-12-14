from django.shortcuts import render
from .models import Categoria

def mostrarCategorias(request):
    p = Categoria.objects.all()
    ctx = {}
    ctx['temas'] = p

    return render(request, 'base/categorias.html', ctx)
