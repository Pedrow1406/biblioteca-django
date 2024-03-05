from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livro, Categoria, Emprestimo
from .forms import CadastroLivro, CadastroCategoria, CadastroEmprestimo
from datetime import date
# Create your views here.
def home(request):
    user_session = request.session.get('usuario') # Retorna None se essa session não existir
    if user_session:
        usuario = Usuario.objects.get(id = user_session)
        livros = Livro.objects.filter(usuario= user_session)
        user_categorias = Categoria.objects.filter(usuario_id = user_session)
        cadastro_livro = CadastroLivro()
        cadastro_livro.fields['dono_livro_cadastrado'].initial = user_session
        cadastro_livro.fields['usuario'].initial = user_session
        cadastro_livro.fields['categoria'].queryset = Categoria.objects.filter(usuario_id = user_session)
        cadastro_livro.fields['categoria'].empty_label = None # Remove a opção nula "-------------"

        cadastro_categoria = CadastroCategoria()
        cadastro_categoria.fields['usuario'].initial = user_session

        cadastro_emprestimo = CadastroEmprestimo()
        cadastro_emprestimo.fields['nome_emprestado'].queryset = Usuario.objects.exclude(id = user_session)
        cadastro_emprestimo.fields['livro'].queryset = Livro.objects.filter(usuario = user_session)
        cadastro_emprestimo.fields['dono_livro_atual'].initial = user_session
        
        emprestimo = Emprestimo.objects.first()
        avaliacao_choices = emprestimo.choices
        return render(request, 'lista_livros.html', context={'livros': livros,
                                                             'v':False, 
                                                             'usuario':usuario,
                                                             'usuario_logado': user_session,
                                                             'cadastro_livro':cadastro_livro,
                                                             'cadastro_categoria':cadastro_categoria,
                                                             'cadastro_emprestimo': cadastro_emprestimo,
                                                             'avaliacao_choices':avaliacao_choices})
    return redirect('/auth/login/?permission=denied')

  
def ver_livro(request, id):
    if request.method == 'GET':
        user_session = request.session.get('usuario')
        if user_session:
            livro = Livro.objects.get(id = id)
            user_categorias = Categoria.objects.filter(usuario_id = user_session)
            emprestimos = Emprestimo.objects.filter(livro=livro)
            emprestimo_recente = Emprestimo.objects.filter(livro=livro).last()
            cadastro_livro = CadastroLivro()
            cadastro_livro.fields['dono_livro_cadastrado'].initial = user_session
            cadastro_livro.fields['usuario'].initial = user_session
            cadastro_livro.fields['categoria'].queryset = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            cadastro_livro.fields['categoria'].empty_label = None # Remove a opção nula "-------------"

            cadastro_categoria = CadastroCategoria()
            cadastro_categoria.fields['usuario'].initial = user_session

            cadastro_emprestimo = CadastroEmprestimo()
            cadastro_emprestimo.fields['dono_livro_atual'].initial = user_session
            cadastro_emprestimo.fields['nome_emprestado'].queryset = Usuario.objects.exclude(id = user_session)
            cadastro_emprestimo.fields['livro'].initial = livro
            cadastro_emprestimo.fields['livro'].queryset = Livro.objects.filter(id = id)
            cadastro_emprestimo.fields['livro'].empty_label = None # Remove a opção nula "-------------"
            cadastro_emprestimo.fields['livro'].widget.attrs['readonly'] = True
            emprestimo = Emprestimo.objects.first()
            avaliacao_choices = emprestimo.choices
            if livro.usuario.id == user_session:
                return render(request, 'ver_livro.html', {'livro':livro,
                                                            'v':True,
                                                            'user_categorias': user_categorias,
                                                            'emprestimos':emprestimos,
                                                            'emprestimo_recente':emprestimo_recente,
                                                            'usuario_logado': user_session,
                                                            'cadastro_livro':cadastro_livro,
                                                            'cadastro_categoria':cadastro_categoria,
                                                            'cadastro_emprestimo': cadastro_emprestimo,
                                                            'avaliacao_choices':avaliacao_choices})
        return redirect('/auth/login/?permission=denied')
    elif request.method == 'POST':
        nome_livro = request.POST.get('nome_livro')
        autor = request.POST.get('autor')
        co_autor = request.POST.get('co_autor')
        is_emprestado = request.POST.get('emprestado')
        categoria =  request.POST.get('categoria_select')
        dados = [nome_livro, autor, co_autor, categoria]
        for dado in dados:
            if dado:
                print(dado)
        if is_emprestado:
            print('Emprestado')
        else:
            print('Não Emprestado')
        return HttpResponse('Dados Enviados com Sucesso')
    

def cadastrar_livro(request):
    user_session = request.session.get('usuario')
    if request.method == 'POST':
        print(request.POST)
        cadastrar_livro = CadastroLivro(request.POST)
        usuario_id = int(request.POST.get('usuario'))
        dono_livro = int(request.POST.get('dono_livro_cadastrado'))
        if user_session:
            if cadastrar_livro.is_valid():
                if usuario_id == user_session and dono_livro == user_session:
                    cadastrar_livro.save()
                    return redirect('/livro/home/?cl=success')
                return redirect('/livro/home/?cl=fail')
            return redirect('/livro/home/?dados=invalidos')
        return redirect('/auth/login/?permission=denied')
    return HttpResponse('Você não pode acessar essa url dessa maneira')

def cadastrar_categoria(request):
    user_session = request.session.get('usuario')
    if request.method == 'POST':
        print(request.POST)
        cadastro_categoria = CadastroCategoria(request.POST)
        usuario_id = int(request.POST.get('usuario'))
        if user_session:
            if cadastro_categoria.is_valid():
                if usuario_id == user_session:
                    cadastro_categoria.save()
                    return redirect('/livro/home/?cc=success')
                return redirect('/livro/home/?cc=fail')
            return redirect('/livro/home/?dados=invalidos')
        return redirect('/auth/login/?permission=denied')
    return HttpResponse('Você não pode acessar essa url dessa maneira')
        
def cadastrar_emprestimo(request):
    user_session = request.session.get('usuario')
    if request.method == 'POST':
        cadastrar_emprestimo = CadastroEmprestimo(request.POST)
        dono_livro_atual = int(request.POST.get('dono_livro_atual'))
        if user_session:
            if cadastrar_emprestimo.is_valid():
                if user_session == dono_livro_atual:
                    user_emprestado = int(request.POST.get('nome_emprestado'))
                    usuario_emprestado = Usuario.objects.get(id = user_emprestado)
                    livro_emprestado = int(request.POST.get('livro'))
                    livro_emprestado = Livro.objects.get(id = livro_emprestado)
                    if livro_emprestado.usuario.id == dono_livro_atual: # Verificando se o dono_livro_atual é realmente dono do livro
                        if usuario_emprestado.id != user_session:
                            livro_emprestado.emprestado = True
                            livro_emprestado.usuario = usuario_emprestado
                            livro_emprestado.save()
                            cadastrar_emprestimo.save()
                            return redirect('/livro/home/?e=success')
                        return HttpResponse('Você não pode emprestar um livro para si mesmo')
                    return HttpResponse('Você não é dono desse livro')
                return HttpResponse('Você esta tentando alterar os dados do usuario atual')
            return HttpResponse('Esse formulario não é valido')
        return HttpResponse('Você precisa esta logado')
    return HttpResponse('Você não pode acessar a URL dessa maneira.')

def devolver_livro(request,id):
    user_session = request.session.get('usuario')
    livro = Livro.objects.get(id=id)
    if user_session:
        if user_session == livro.usuario.id:
            avaliacao = request.POST.get('avaliacao')
            print(avaliacao)
            print(livro.id)
            emprestimo = Emprestimo.objects.filter(livro=livro).last()
            emprestimo.data_devolucao = date.today()
            livro.emprestado = False
            livro.usuario = emprestimo.dono_livro_atual
            livro.save()
            emprestimo.avaliacao = avaliacao
            emprestimo.save()
            print(emprestimo)
            return redirect('/livro/home/?l=d')

def deletar_livro(request,id):
    user_session = request.session.get('usuario')
    if user_session:
        livro = Livro.objects.get(id=id)
        user = Usuario.objects.get(id=user_session)
        if user.id == livro.usuario.id:
            livro.delete()
            return redirect('/livro/home/?l=deleted')
        return redirect('/livro/home/?l=deleted_fail')
    return redirect('/auth/login/?permission=denied')
