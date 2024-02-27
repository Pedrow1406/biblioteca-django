from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('username', 'email', 'data_nascimento', 'senha')