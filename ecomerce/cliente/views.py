from django.shortcuts import render
from .models import Cliente
from produto.models import Produto, ListImages, Categoria
from .forms import FormCriarCliente
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
  produtos = Produto.objects.filter(status="o")[:6]
  categorias = Categoria.objects.all()
  return render(request, "cliente/index.html", {
    "produtos": produtos,
    "categorias": categorias,
  })

def criar_conta(request):
  if request.method == "POST":
    form = FormCriarCliente(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      user = User(username=form.cleaned_data['nome'],email=form.cleaned_data['email'],password=form.cleaned_data['cpf'])
      user.save()
      return HttpResponseRedirect(reverse('cliente:index'))
  else:
    form = FormCriarCliente()
  return render(request, "cliente/criar_conta.html", {
      "form": form,
  })
