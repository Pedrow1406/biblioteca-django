from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Livro)
admin.site.register(models.Categoria)
admin.site.register(models.Emprestimo)