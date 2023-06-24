from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from cliente.models import Cliente,Empresa, PessoaFisica
from .models import Carrinho, ItemCarrinho, Compra
from produto.models import Produto
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime

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

def get_itens_car(carrinho):
  try:
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)
    return itens
  except ObjectDoesNotExist:
    return None

def index(request):
  cliente = get_cliente(request.user.username)
  carrinhos = get_carrinhos(cliente)
  compras = Compra.objects.filter(carrinho__cliente=cliente).order_by('-id')[:3]
  
  #caso em que não tem carrinho
  if not carrinhos.exists():
    car = Carrinho(cliente=cliente)
    car.save()

  car_atual = {}
  carrinhos_closed = []

  for c in carrinhos:
    if c.close_car:
      item = {}
      itens_car = ItemCarrinho.objects.filter(carrinho=c)
      item['carrinho'] = c
      item['produtos'] = itens_car
      carrinhos_closed.append(item)
    else:
      itens_car_atual = ItemCarrinho.objects.filter(carrinho=c)
      aux_car = {'carrinho': c, 'produtos': itens_car_atual}
      car_atual.update(aux_car)
      
  return render(request, "carrinho/index.html",{
    "cliente": cliente,
    "carrinhos": carrinhos,
    "car_atual": car_atual,
    "carrinhos_closed": carrinhos_closed,
    "compras": compras,
  })
  
def create(request):
  nome = request.POST["nome_car"]
  cliente = get_cliente(request.user.username)
  carrinho = Carrinho(nome=nome,cliente=cliente)
  carrinho.save()
  return HttpResponseRedirect(reverse('carrinho:index'))
  
def delete(request, id):
  carrinho = Carrinho.objects.get(id=id)
  itens = ItemCarrinho.objects.filter(carrinho=carrinho)
  for i in itens:
    i.delete()
  carrinho.delete()
  return HttpResponseRedirect(reverse('carrinho:index'))
  
def upgrade_preco_total(car):
  itens = ItemCarrinho.objects.filter(carrinho=car)
  preco = 0
  for i in itens:
    preco += i.preco_acumulado
  car.preco_total = preco
  car.save()
  
def upgrade_carrinho(car, item, op):
  item.preco_acumulado = item.produto.price * item.quantidade
  item.save()
  if op == "add":
    car.qtd_produtos += 1
    upgrade_preco_total(car)
  elif op == "remove":
    car.qtd_produtos -= 1
    upgrade_preco_total(car)
  
def add_item(request, cod):
  cliente = get_cliente(request.user.username)
  produto = Produto.objects.get(codigo=cod)
  carrinhos = get_carrinhos(cliente)
  
  if carrinhos:
    for c in carrinhos:
      if not c.close_car:
        car = c
        break
  else:
    car = Carrinho(cliente=cliente)
    car.save()
  itens = get_itens_car(car)
  search = False

  if itens:
    for i in itens:
      if i.produto == produto:
        search = True
        add_qtd(request, i.produto.codigo)
        break
    if search == False:
      item = ItemCarrinho(carrinho=car,produto=produto)
      item.save()
      upgrade_carrinho(car, item, "add")
  else:
    item = ItemCarrinho(carrinho=car,produto=produto)
    item.save()
    upgrade_carrinho(car, item, "add")

  return HttpResponseRedirect(reverse('carrinho:index'))
  
def remove_item(request, cod, id):
  produto = Produto.objects.get(codigo=cod)
  cliente = get_cliente(request.user.username)
  carrinho1 = Carrinho.objects.get(id=id)
  item = ItemCarrinho.objects.filter(carrinho=carrinho1,produto=produto)
  for i in item:
    carrinho1.qtd_produtos -= i.quantidade
    i.delete()
    carrinho1.save()
    upgrade_preco_total(carrinho1)
  
  return HttpResponseRedirect(reverse('carrinho:index'))
  
def add_qtd(request, cod):
  cliente = get_cliente(request.user.username)
  produto = Produto.objects.get(codigo=cod)
  carrinhos = get_carrinhos(cliente)
  
  if carrinhos:
    for c in carrinhos:
      if not c.close_car:
        car = c
        break
  else:
    car = Carrinho(cliente=cliente)
    car.save()
  item = ItemCarrinho.objects.get(carrinho=car, produto=produto)
  if item.quantidade < item.produto.quantidade:
    item.quantidade += 1
    item.save()
    upgrade_carrinho(car,item,"add")
  return HttpResponseRedirect(reverse('carrinho:index'))
  
def remove_qtd(request, cod):
  cliente = get_cliente(request.user.username)
  produto = Produto.objects.get(codigo=cod)
  carrinhos = get_carrinhos(cliente)
  if carrinhos:
    for c in carrinhos:
      if not c.close_car:
        carrinho1 = c
        break
  
  item = ItemCarrinho.objects.get(carrinho=carrinho1,produto=produto)
  if item.quantidade == 1:
    remove_item(request, item.produto.codigo, carrinho1.id)
  else:
    item.quantidade -= 1
    item.save()
    upgrade_carrinho(carrinho1,item,"remove")
  return HttpResponseRedirect(reverse('carrinho:index'))
  
def close_compra(request, id):
  cliente = get_cliente(request.user.username)
  carrinho = Carrinho.objects.get(id=id)
  itens_car = get_itens_car(carrinho)
      
  for i in itens_car:
    i.produto.quantidade -= i.quantidade
    i.produto.save()
    if i.produto.quantidade <= 0:
      i.produto.status = "f"
      i.produto.save()
      
  carrinho.close_car = True
  carrinho.save()
  cliente.total_compras += 1
  cliente.total_gasto += carrinho.preco_total
  cliente.save()
  new_car = Carrinho(cliente=cliente)
  new_car.save()
  data_atual = datetime.now()
  compra = Compra(carrinho=carrinho,status='pp',data=data_atual)
  compra.save()
  return HttpResponseRedirect(reverse('cliente:perfil'))
