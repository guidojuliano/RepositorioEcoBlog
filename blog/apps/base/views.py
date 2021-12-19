from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Categoria, Post, Web
from django.urls import reverse_lazy
from .forms import forms_postear
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def mostrarCategorias(request):
    p = Categoria.objects.all()
    ctx = {}
    ctx['temas'] = p

    return render(request, 'base/categorias.html', ctx)
#vista de mostrar todos los post
def mostrarPost(request):
    p = Post.objects.all()
    
    ctx = {}
    ctx['posts'] = p

    return render(request, 'base/posts.html', ctx)

#vista de mostrar el post completo

def PostCompleto(request, pk):
    post = Post.objects.get(pk = pk)
    likes = post.cantidad_likes
    ctx = {}
    ctx['complete_post'] = post
    ctx['likes'] = likes

    return render(request, 'base/detallePost.html', ctx)
    
    

def mostrarSobreNosotros(request):
    p = Web.objects.all()
    ctx = {}
    ctx['nosotros'] = p

    return render(request, 'base/nosotros.html', ctx)


class Postear(LoginRequiredMixin, CreateView):
    model = 'Post'
    template_name = 'base/postear.html'
    form_class = forms_postear
    success_url = reverse_lazy('base:mostrar_categorias')

@login_required
def darLike(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('/post/'+str(post.pk))

def filtroporCategoria(request, pk):
    categoria = Categoria.objects.get(pk = pk)
    p = Post.objects.filter(categoria = categoria)

    ctx = {}
    ctx['category'] = categoria
    ctx['post'] = p

    return render(request, 'base/filtroxCategoria.html', ctx)

