from django.shortcuts import render
from .models import Cliente, PessoaFisica, Empresa
from produto.models import Produto, ListImages, Categoria
from .forms import FormCriarCliente
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
    if request.method == 'POST':
        form = FormCriarCliente(request.POST,request.FILES)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data["username"],email=form.cleaned_data["email"],password=form.cleaned_data["password"])
            user.save()
            form.save()
            return HttpResponseRedirect(reverse('cliente:index'))
    else:
        form = FormCriarCliente()
    return render(request, 'cliente/criar_conta.html', {'form': form})

def perfil(request, id):
  cliente = Cliente.objects.get(id=id)
  return render(request, "cliente/perfil.html", {
    "cliente": cliente,
  })
  
def tipocliente(request):
  if request.method == "POST":
    if request.POST["tipo"] == "pessoa":
      return HttpResponseRedirect(reverse('cliente:criar_pessoa'))
    elif request.POST["tipo"] == "empresa":
      return HttpResponseRedirect(reverse('cliente:criar_empresa'))
  else:
    return render(request, "cliente/type_cliente.html")
    
def criar_pessoa(request):
  return render(request, "cliente/criar_pessoa_fisica.html")
  
def criar_empresa(request):
  return render(request, "cliente/criar_empresa.html")