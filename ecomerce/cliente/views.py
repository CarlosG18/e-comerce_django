from django.shortcuts import render
from .models import Cliente
from produto.models import Produto, ListImages, Categoria
from .forms import FormCriarCliente
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
  return render(request, "cliente/login.html")

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
