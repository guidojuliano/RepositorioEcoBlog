from django.db import models
from ckeditor.fields import RichTextField

class ModeloBase(models.Model):
    id: models.AutoField(primary_key= True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la Categoria', max_lenght = 100, unique=True)
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to = 'categoria/')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre

class Autor(ModeloBase):
    pass

class Post (ModeloBase):
    titulo = models.CharField('Titulo del Post', max_length=150, unique=True)
    slug = models.CharField('Slug', max_length=150, unique=True)
    descripcion = models.TextField('Descripcion')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to = 'media/', max_length=255)
    publicado = models.BooleanField('Publicado / No Publicado', default=False)
    fecha_publicacion = models.DateField('Fecha de Publicacion')
