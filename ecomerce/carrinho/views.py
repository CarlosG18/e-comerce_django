from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from cliente.models import Cliente,Empresa, PessoaFisica
from .models import Carrinho, ItemCarrinho
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
  return render(request, "carrinho/index.html",{
    "cliente": cliente,
    "carrinhos": carrinhos,
  })
  
def create(request):
  cliente = get_cliente(request.user.username)
  carrinho = Carrinho(cliente=cliente)
  carrinho.save()
  return HttpResponseRedirect(reverse('carrinho:index'))
  
def delete(request, id):
  carrinho = Carrinho.objects.get(id=id)
  carrinho.delete()
  return HttpResponseRedirect(reverse('carrinho:index'))