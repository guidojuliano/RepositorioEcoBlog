
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroUser
        

class VistaRegistro(CreateView):
    form_class = RegistroUser
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')
            
