from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from .models import Users
import re

# Create your views here.
def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == 'GET':
        return render(request, 'accounts/cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
       
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('cadastro')
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            messages.add_message(request,messages.ERROR,'email invalido!')
            return redirect('cadastro') 
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Digite as senhas iguais')
            return redirect('cadastro')
        try:
            user = Users.objects.create_user(# type: ignore 
                username=nome,
                email=email,
                password=senha
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
            return redirect('login')
        except: 
            messages.add_message(request, constants.ERROR, 'Erro Interno do sistema tente novamente mais tarde')
            return render(request, 'accounts/cadastro.html')

def logar(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha)
        
        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha incorreto')
            return render(request, 'accounts/login.html')

def editar_user(request, id):
    if request.method == 'GET':
        return render(request, 'accounts/editar_user.html')
        
def sair(request):
    logout(request)
    return redirect('/')