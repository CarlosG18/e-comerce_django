from django.shortcuts import render
from cliente.models import Empresa, PessoaFisica
from produto.models import Produto,Categoria
from .forms import FormPessoaFisica,FormEmpresa, FormUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required
def index(request):
  produtos = Produto.objects.filter(status="o")[:6]
  categorias = Categoria.objects.all()
  return render(request, "cliente/index.html", {
    "produtos": produtos,
    "categorias": categorias,
  })

def perfil(request):
  user = User.objects.get(username=request.user.username)
  group = user.groups.all()

  for g in group:
    if g.name == 'pessoafisica':
      request.session['grupo'] = 'pessoafisica'
      cliente = PessoaFisica.objects.get(user=user)
      return render(request, "cliente/perfil.html",{
        "cliente": cliente,
      })
    elif g.name == 'empresa':
      request.session['grupo'] = 'empresa'
      cliente = Empresa.objects.get(user=user)
      return render(request, "cliente/perfil.html",{
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
  if request.method == "POST":
    form_user = FormUser(request.POST)
    form = FormPessoaFisica(request.POST,request.FILES)
    if form.is_valid() and form_user.is_valid():
      user = User.objects.create_user(username=form_user.cleaned_data["username"], email=form_user.cleaned_data["email"], password=form_user.cleaned_data["password"]) 
      user.save()
      user.groups.add(Group.objects.get(name='pessoafisica'))
      cliente = form.save(commit=False)
      cliente.user = user
      cliente.save()
      return HttpResponseRedirect(reverse('login'))
  else:
    form_user = FormUser()
    form_pessoa = FormPessoaFisica()
  return render(request, "cliente/criar_pessoa_fisica.html",{
      "form_pessoa": form_pessoa,
      "form_user": form_user,
  })

def criar_empresa(request):
  if request.method == "POST":
    form_user = FormUser(request.POST)
    form = FormEmpresa(request.POST,request.FILES)
    if form.is_valid() and form_user.is_valid():
      user = User.objects.create_user(username=form_user.cleaned_data["username"], email=form_user.cleaned_data["email"], password=form_user.cleaned_data["password"]) 
      user.save()
      user.groups.add(Group.objects.get(name='empresa'))
      cliente = form.save(commit=False)
      cliente.user = user
      cliente.save()
      return HttpResponseRedirect(reverse('login'))
  else:
    form_user = FormUser()
    form = FormEmpresa()
  return render(request, "cliente/criar_empresa.html",{
      "form_emp": form,
      "form_user": form_user,
  })