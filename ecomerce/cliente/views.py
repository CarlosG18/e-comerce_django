from django.shortcuts import render
from cliente.models import Empresa, PessoaFisica
from produto.models import Produto,Categoria
from carrinho.models import Compra,Carrinho
from .forms import FormPessoaFisica,FormEmpresa, FormUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group
import django

# help(Group) - olhar a documentação

def get_cliente(username):
  user = User.objects.get(username=username)
  try:
    cliente = PessoaFisica.objects.get(user=user)
    return cliente
  except ObjectDoesNotExist:
    cliente = Empresa.objects.get(user=user)
    return cliente
    
def notaMedia():
  produtos = Produto.objects.all()
  cont = 0
  nota_geral = 0
  
  for p in produtos:
    if p.media_stars != 0:
      cont += 1
      nota_geral += p.media_stars
  return nota_geral/cont

@login_required
def index(request):
  #visitas = request.session.get("visitas",0)
  #request.session["visitas"] = visitas+1
  
  produtos = Produto.objects.filter(status="o")[:6]
  produtos_music = Produto.objects.filter(categoria__nome='Música')[:3]
  produtos_tech = Produto.objects.filter(categoria__nome='Tecnologia')[:3]
  categorias = Categoria.objects.all()
  nota = notaMedia()
  produtos_avaliados = Produto.objects.filter(media_stars__gte=nota)[:3]
  cliente = get_cliente(request.user.username)
  return render(request, "cliente/index.html", {
    "produtos": produtos,
    "produtos_music": produtos_music,
    "produtos_tech": produtos_tech,
    "categorias": categorias,
    "cliente": cliente,
    "produtos_avaliados": produtos_avaliados,
  })
  
def get_carrinhos(cliente):
  try:
    carrinhos = Carrinho.objects.filter(cliente=cliente)
    return carrinhos
  except ObjectDoesNotExist:
    return None
  
@login_required
def perfil(request):
  cliente = get_cliente(request.user.username)
  carrinhos = get_carrinhos(cliente)
  if carrinhos:
    carrinho = carrinhos[0]
    compra = Compra.objects.filter(carrinho=carrinho)
  else:
    compra = None
  
  return render(request, "cliente/perfil.html",{
    "cliente": cliente,
    "compra": compra,
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
      #user.groups.add(Group.objects.get(name='pessoafisica'))
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
      #user.groups.add(Group.objects.get(name='empresa'))
      cat = Categoria(nome=form.cleaned_data["segmento"])
      cat.save()
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