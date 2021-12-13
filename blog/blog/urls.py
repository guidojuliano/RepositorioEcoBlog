from os import replace
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from . import views
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name='Inicio'),
    path('login/', auth.LoginView.as_view(template_name="usuarios/login.html"), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'media/(?P<path>.*)$', serve, {
            'document_root':settings.MEDIA_ROOT,
        })
    ]