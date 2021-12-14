from django.urls import path
from .views import VistaRegistro

urlpatterns = [
    path('signup/', VistaRegistro.as_view(), name='signup')
]
