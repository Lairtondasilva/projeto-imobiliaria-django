from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Imovel
# Create your views here.

@login_required(login_url="login")
def home(request):
  imoveis = Imovel.objects.all()
    return render('home.html',{'imoveis':imoveis})
