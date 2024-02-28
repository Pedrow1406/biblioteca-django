from django.db import models
from usuarios.models import Usuario
# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome
    
class Livro(models.Model):
    nome = models.CharField(max_length=60)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length = 30, blank=True)
    data_emprestimo = models.DateTimeField(null=True, blank=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    tempo_duracao = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome