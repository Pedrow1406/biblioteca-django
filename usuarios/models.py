from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.username