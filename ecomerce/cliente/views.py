from django.shortcuts import render
from .models import UserPessoaFisica, UserEmpresa
from produto.models import Produto, ListImages, Categoria
from .forms import FormUserPessoaFisica,FormUserEmpresa
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

# def perfil(request, id):
#   cliente = Cliente.objects.get(id=id)
#   return render(request, "cliente/perfil.html", {
#     "cliente": cliente,
#   })
  
def tipocliente(request):
  if request.method == "POST":
    if request.POST["tipo"] == "pessoa":
      return HttpResponseRedirect(reverse('cliente:criar_pessoa'))
    elif request.POST["tipo"] == "empresa":
      return HttpResponseRedirect(reverse('cliente:criar_empresa'))
  else:
    return render(request, "cliente/type_cliente.html")
    
def criar_pessoa(request):
  if request.method == "POST":
    form = FormUserPessoaFisica(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('cliente:index'))
  else:
    form = FormUserPessoaFisica()
  return render(request, "cliente/criar_pessoa_fisica.html", {
      "form": form,
  })
  
def criar_empresa(request):
  if request.method == "POST":
    form = FormUserEmpresa(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('cliente:index'))
  else:
    form = FormUserEmpresa()
  return render(request, "cliente/criar_empresa.html",{
      "forms": form,
  })