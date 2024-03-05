from django.db import models
from usuarios.models import Usuario
# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=60)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    dono_livro_cadastrado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='dono_livro_cadastrado')
    def __str__(self) -> str:
        return self.nome
    
class Emprestimo(models.Model):
    choices = (
        ('P', 'Pessimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Otimo')
    )
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True, blank=True)
    dono_livro_atual = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='dono_livro_atual')
    nome_emprestado_anonimo = models.CharField(max_length = 30, blank=True)
    data_emprestimo = models.DateField(auto_now_add=True, null=True, blank=True)
    data_devolucao = models.DateField(null=True, blank=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)

    def __str__(self) -> str:
        if self.nome_emprestado:
            return (f'{self.nome_emprestado} | {self.livro}')
        return (f'{self.nome_emprestado_anonimo} | {self.livro}')

