from django.shortcuts import render
from .models import Cliente
from produto.models import Produto, ListImages, Categoria
from .forms import UserClienteForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
  produtos = Produto.objects.filter(status="o")[:6]
  categorias = Categoria.objects.all()
  return render(request, "cliente/index.html", {
    "produtos": produtos,
    "categorias": categorias,
  })

def criar_conta(request):
  if request.method == "POST":
    form = UserClienteForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('cliente:index'))
  else:
    form = UserClienteForm()
  return render(request, "cliente/criar_conta.html", {
      "form": form,
  })
