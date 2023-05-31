from django.shortcuts import render
from .models import Cliente
from produto.models import Produto, ListImages, Categoria
from .forms import FormCriarCliente, FormLogin
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
  produtos = Produto.objects.filter(status="o")[:6]
  categorias = Categoria.objects.all()
  return render(request, "cliente/index.html", {
    "produtos": produtos,
    "categorias": categorias,
  })

def login(request):
  if request.method == "POST":
    form = FormLogin(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('cliente:criar_conta'))
  else:
    form = FormCriarCliente()
  return render(request, "cliente/login.html", {
      "form": form,
  })

def criar_conta(request):
  if request.method == "POST":
    form = FormCriarCliente(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('cliente:index'))
  else:
    form = FormCriarCliente()
  return render(request, "cliente/criar_conta.html", {
      "form": form,
  })
