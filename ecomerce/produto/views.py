from django.shortcuts import render
from .models import Produto, ListImages, Comentario
from .forms import FormProduto, FormImages, FormComentario
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from cliente.models import Empresa
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required
import random as r
from cliente.models import Cliente, PessoaFisica, Empresa
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

def get_cliente(username):
  user = User.objects.get(username=username)
  try:
    cliente = PessoaFisica.objects.get(user=user)
    return cliente
  except ObjectDoesNotExist:
    cliente = Empresa.objects.get(user=user)
    return cliente

class ProdutoListView(generic.ListView):
  model = Produto
  context_object_name = "produtos"
  template_name = "produto/index.html"
  paginate_by = 10
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = User.objects.get(username=self.request.user.username)
    try: 
      cliente = PessoaFisica.objects.get(user=user)
      context['user'] = user
      context['cliente'] = cliente
      return context
    except ObjectDoesNotExist:
      cliente = Empresa.objects.get(user=user)
      context['user'] = user
      context['cliente'] = cliente
      return context

def update_stars(produto,comentarios):
  if comentarios:
    stars = 0
    qtd_comentarios = comentarios.count()
    for c in comentarios:
      stars += c.stars
    media = stars/qtd_comentarios
    produto.media_stars = media
    produto.save()
  else:
    produto.media_stars = 0.00
    produto.save()
  
def detail(request, cod):
  produto = Produto.objects.get(codigo=cod)
  list_imgs = ListImages.objects.filter(produto__codigo=cod)
  comentarios = Comentario.objects.filter(produto__codigo=cod)
  update_stars(produto,comentarios)
  cliente = get_cliente(request.user.username)
  
  if request.method == 'POST':
    form = FormComentario(request.POST)
    if form.is_valid():
      comentario = form.save(commit=False)
      comentario.produto = produto
      comentario.cliente = cliente
      comentario.save()
      return HttpResponseRedirect(reverse('produto:detail', args=[cod]))
  else:
    form = FormComentario()
  return render(request, "produto/detail.html", {
    "produto": produto,
    "list_imgs": list_imgs,
    "comentarios": comentarios,
    "cliente": cliente,
    "form": form,
  })
  
def hash_cod(nome,price,qtd):
  codigo = ""
  cont = 0
  price_int = int(price)
  tabela_vogal = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5',
  }
  
  while cont<9:
    for letra in nome:
      for vogal,peso in tabela_vogal.items():
        if letra == vogal:
          codigo += peso
          cont += 1
          break
        else:
          num = r.randint(0,(qtd*cont)%10)
          codigo += str(num)
          cont += 1
          break
  
  int_codigo = int(codigo)
  return int_codigo

@login_required
def add(request):
  user = User.objects.get(username=request.user.username)
  empresa = Empresa.objects.get(user=user)

  if request.method == "POST":
    form = FormProduto(request.POST, request.FILES)
    if form.is_valid():
      produto = form.save(commit=False)
      produto.media_stars = 0.00
      produto.loja = empresa
      produto.codigo = hash_cod(form.cleaned_data["nome"],form.cleaned_data["price"],form.cleaned_data["quantidade"])
      produto.save()
      return HttpResponseRedirect(reverse('produto:produtos_emp'))
  else:
    form = FormProduto()
  return render(request, "produto/add.html", {
    "form": form,
  })
  
def categoria(request, cat):
  produtos = Produto.objects.filter(categoria__nome=cat)
  cliente = get_cliente(request.user.username)
  return render(request, "produto/index.html", {
    "produtos": produtos,
    "categoria": cat,
    "cliente": cliente,
  })

@login_required
def add_fotos(request, cod):
  produto = Produto.objects.filter(codigo=cod).get()
  
  if request.method == "POST":
    form = FormImages(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('produto:detail', args=[cod]))
  else:
    initial_data = {'produto': produto}
    form = FormImages(initial=initial_data)
  return render(request, "produto/add_fotos.html", {
    "produto": produto,
    "form": form,
  })

@login_required
def remove(request, cod):
  produto = Produto.objects.get(codigo=cod)
  produto.delete()
  return HttpResponseRedirect(reverse('produto:produtos_emp'))

@login_required
def remove_img(request, id):
  img = ListImages.objects.get(id=id)
  produto = img.produto
  cod = produto.codigo
  img.delete()
  return HttpResponseRedirect(reverse('produto:detail', args=[cod]))

def produtos_emp(request):
  empresa = Empresa.objects.get(user__username=request.user.username)
  produtos = Produto.objects.filter(loja=empresa)
  user = User.objects.get(username=request.user.username)
  cliente = get_cliente(request.user.username)
  return render(request, "produto/index.html", {
    "produtos": produtos,
    "user": user,
    "cliente": cliente,
  })
  
def remove_comentario(request, id, cod):
  comentario = Comentario.objects.get(id=id)
  comentario.delete()
  produto = Produto.objects.get(codigo=cod)
  comentarios = Comentario.objects.filter(produto__codigo=cod)
  update_stars(produto,comentarios)
  return HttpResponseRedirect(reverse('produto:detail', args=[cod]))
  
def estoque(request):
  cliente = get_cliente(request.user.username)
  produtos = Produto.objects.filter(loja=cliente)
  produtos_falta = Produto.objects.filter(status="f",loja=cliente)
  produtos_oferta = Produto.objects.filter(status="o",loja=cliente)
  return render(request, "cliente/empresa/estoque.html", {
    "produtos_falta": produtos_falta,
    "produtos_oferta": produtos_oferta,
    "produtos": produtos,
  })


def estoque_up(request, cod):
  produto = Produto.objects.get(codigo=cod)
  qtd_produto = request.POST['qtd_produto']
  produto.quantidade = qtd_produto
  produto.status = 'n'
  produto.save()
  return HttpResponseRedirect(reverse('produto:estoque'))