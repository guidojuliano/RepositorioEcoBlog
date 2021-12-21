from django import forms
from .models import Post

class forms_postear(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'categoria', 'contenido', 'imagen_referencial']