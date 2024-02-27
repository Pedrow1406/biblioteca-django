from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
# Create your views here.
def home(request):
    user_session = request.session.get('usuario') # Retorna None se essa session não existir
    if user_session:
        usuario = Usuario.objects.get(id = user_session).username
        return HttpResponse(f'Olá {usuario}. Abaixo está sua lista de livros.')
    return redirect('/auth/login/?permission=denied')