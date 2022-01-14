from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.messages import constants
from django.contrib import  auth
# Create your views here.

def cadastro (request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect("/")
        return render(request,'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if len(username.strip())== 0 or len(senha.strip()) == 0 or len(email.strip())==0:
            messages.add_message(request,constants.ERROR,'preencha todos os campos')
            return redirect('cadastro')
        usuario = User.objects.filter(username=username)
        if usuario.exists():
            messages.add_message(request,constants.ERROR,'Nome de usuário já existe')
            return redirect('cadastro')
        try:
            usuario = User.objects.create_user(username=username,password=senha,email=email)
            usuario.save()
            messages.add_message(request,constants.SUCCESS,'Cadastro realizado com succeso')
            return redirect('login')
        except:
            messages.add_message(request,constants.ERROR,"Erro no sistema")
            return redirect('cadastro')
            
def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render (request,'login.html')
         
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        usuario = auth.authenticate(username=username,password=senha)
        if not usuario:
            messages.add_message(request,constants.ERROR,'Usuário ou senha inválidos')
            return redirect('login')
        else:
            auth.login(request,usuario)
            return redirect('/')
def sair(request):
    auth.logout(request)
    return redirect('login')                    