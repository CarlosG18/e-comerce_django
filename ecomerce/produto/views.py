from django.shortcuts import render
from .models import Produto, ListImages, Comentario
from .forms import FormProduto, FormImages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from cliente.models import Empresa
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required
from cliente.models import Cliente, PessoaFisica, Empresa
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

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
    
def ofertas(request):
  produtos = Produto.objects.all()
  list_imgs = ListImages.objects.all()
  return render(request, "produto/ofertas.html", {
    "produtos": produtos,
    "list_imgs": list_imgs,
  })

def detail(request, cod):
  produto = Produto.objects.get(codigo=cod)
  list_imgs = ListImages.objects.filter(produto__codigo=cod)
  comentarios = Comentario.objects.filter(produto__codigo=cod)
  return render(request, "produto/detail.html", {
    "produto": produto,
    "list_imgs": list_imgs,
    "comentarios": comentarios,
  })

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
      produto.save()
      return HttpResponseRedirect(reverse('produto:index'))
  else:
    form = FormProduto()
  return render(request, "produto/add.html", {
    "form": form,
  })
  
def categoria(request, cat):
  produtos = Produto.objects.filter(categoria__nome=cat)
  return render(request, "produto/list_categoria.html", {
    "produtos": produtos,
    "categoria": cat,
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
  return HttpResponseRedirect(reverse('produto:index'))

@login_required
def remove_img(request, id):
  img = ListImages.objects.get(id=id)
  produto = img.produto
  cod = produto.codigo
  img.delete()
  return HttpResponseRedirect(reverse('produto:detail', args=[cod]))