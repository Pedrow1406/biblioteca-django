from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livro
# Create your views here.
def home(request):
    user_session = request.session.get('usuario') # Retorna None se essa session não existir
    if user_session:
        usuario = Usuario.objects.get(id = user_session)
        livros = Livro.objects.filter(usuario= user_session)
        return render(request, 'lista_livros.html', context={'livros': livros, 'usuario':usuario})
    return redirect('/auth/login/?permission=denied')