from django.contrib import admin

# Register your models here.
from .models import Autor, Comentario, Receta

admin.site.register([Autor,Comentario,Receta])