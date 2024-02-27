from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date, datetime
from . import models 
from django.db.models import Q
from hashlib import sha256

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    elif request.method == 'POST':
        user = request.POST.get('user').strip().capitalize()
        password = request.POST.get('password').strip()
        password_hashed = sha256(password.encode()).hexdigest()
        user_existente = models.Usuario.objects.filter(username=user, senha=password_hashed).first()
        if user_existente:
            id_user = request.session['usuario'] = user_existente.id
            return redirect(f'/livro/home/?id_user={id_user}')
        return redirect('/auth/login/?loged=0')
    
def logout(request):
    request.session.flush()
    return redirect('/auth/login/?logout=1')

def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastrar.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome').strip().capitalize()
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email').lower().strip()
        password = request.POST.get('password').strip()

        def calcula_idade(data_nascimento):
            data_hoje = date.today()
            idade = data_hoje.year - data_nascimento.year
            if (data_hoje.month, data_hoje.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1
            return idade
        
        data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
        idade = calcula_idade(data_nascimento)
        dados = [nome, email, password]
        for dado in dados:
            if ' ' in dado:
                return redirect('/auth/cadastrar/?c=e')
 
        if idade >= 18 and len(password) >= 8 and len(email) >= 9 and len(nome) >= 5:
            password_hashed = sha256(password.encode()).hexdigest()
            user_existente = models.Usuario.objects.filter(Q(email=email) | Q(username=nome)).exists()
            if user_existente:
                return redirect('/auth/cadastrar/?c=ee')
            print(f'Nome: {nome}')
            print(f'Data de Nascimento: {data_nascimento}')
            print(f'Email: {email}')
            print(f'Senha: {password}')
            print(f'Senha Criptografada: {password_hashed}')
            usuario = models.Usuario(username=nome, email=email, senha=password_hashed, data_nascimento=data_nascimento)
            usuario.save()
            return redirect('/auth/cadastrar/?c=1')
        elif idade < 18:
            return redirect('/auth/cadastrar/?c=i')
        return redirect('/auth/cadastrar/?c=0')