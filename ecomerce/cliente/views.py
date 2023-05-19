from django.shortcuts import render
from .models import Cliente
from produto.models import Produto, ListImages

def index(request):
  produtos = Produto.objects.all()
  list_imgs = ListImages.objects.all()
  return render(request, "cliente/index.html", {
    "produtos": produtos,
    "list_img": list_imgs,
  })

def login(request):
  return render(request, "cliente/login.html")

def criar_conta(request):
  return render(request, "cliente/criar_conta.html")
