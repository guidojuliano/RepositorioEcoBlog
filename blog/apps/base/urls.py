from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('categorias/', views.mostrarCategorias, name='mostrar_categorias'),
    path('postear/', views.Postear.as_view(), name="postear"),
    #mostrar todos los post
    path('post/', views.mostrarPost, name='mostrar_post'),
    path('nosotros/', views.mostrarSobreNosotros, name='mostrar_nosotros'),
    path('like/<int:pk>', views.darLike, name='dar_like'),
    #mostrar post en especifico
    path('completePost/<int:pk>', views.PostCompleto, name='complete_post'),
    path('filtro/<int:pk>', views.filtroporCategoria, name='filtro'),
  
]