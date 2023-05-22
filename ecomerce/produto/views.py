from django.shortcuts import render
from .models import Produto, ListImages
from .forms import FormProduto, FormImages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):
  produtos = Produto.objects.all()
  return render(request, "produto/index.html", {
    "produtos": produtos,
  })

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
  return render(request, "produto/detail.html", {
    "produto": produto,
    "list_imgs": list_imgs,
  })

def add(request):
  if request.method == "POST":
    form = FormProduto(request.POST, request.FILES)
    if form.is_valid():
      form.save()
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
  
def remove(request, cod):
  produto = Produto.objects.get(codigo=cod)
  produto.delete()
  return HttpResponseRedirect(reverse('produto:index'))
  
def remove_img(request, id):
  img = ListImages.objects.get(id=id)
  produto = img.produto
  cod = produto.codigo
  img.delete()
  return HttpResponseRedirect(reverse('produto:detail', args=[cod]))