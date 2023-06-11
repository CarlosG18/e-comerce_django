from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from cliente.models import Cliente,Empresa, PessoaFisica
from .models import Carrinho, ItemCarrinho
from produto.models import Produto
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponseRedirect

def get_cliente(username):
  user = User.objects.get(username=username)
  try:
    cliente = PessoaFisica.objects.get(user=user)
    return cliente
  except ObjectDoesNotExist:
    cliente = Empresa.objects.get(user=user)
    return cliente
    
def get_carrinhos(cliente):
  try:
    carrinhos = Carrinho.objects.filter(cliente=cliente)
    return carrinhos
  except ObjectDoesNotExist:
    return None

def index(request):
  cliente = get_cliente(request.user.username)
  carrinhos = get_carrinhos(cliente)
  if carrinhos:
    carrinho1 = carrinhos[0]
    itens_car = ItemCarrinho.objects.filter(carrinho=carrinho1)
  else:
    itens_car = None
  return render(request, "carrinho/index.html",{
    "cliente": cliente,
    "carrinhos": carrinhos,
    "itens_car": itens_car,
  })
  
def create(request):
  nome = request.POST["nome_car"]
  cliente = get_cliente(request.user.username)
  carrinho = Carrinho(nome=nome,cliente=cliente)
  carrinho.save()
  return HttpResponseRedirect(reverse('carrinho:index'))
  
def delete(request, id):
  carrinho = Carrinho.objects.get(id=id)
  carrinho.delete()
  return HttpResponseRedirect(reverse('carrinho:index'))
  
def add_item(request, cod):
  cliente = get_cliente(request.user.username)
  produto = Produto.objects.get(codigo=cod)
  carrinhos = get_carrinhos(cliente)
  for car in carrinhos:
    item = ItemCarrinho(carrinho=car,produto=produto)
    item.save()
  return HttpResponseRedirect(reverse('cliente:index'))
  
def remove_item(request, cod):
  produto = Produto.objects.get(codigo=cod)
  cliente = get_cliente(request.user.username)
  carrinhos = get_carrinhos(cliente)
  carrinho1 = carrinhos[0]
  
  item = ItemCarrinho(carrinho=carrinho1,produto=produto)
  item.carrinho = None
  item.save()
  
  return HttpResponseRedirect(reverse('carrinho:index'))