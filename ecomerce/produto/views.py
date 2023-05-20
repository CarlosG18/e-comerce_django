from django.shortcuts import render
from .models import Produto, ListImages
from .forms import FormProduto
from django.http import HttpResponseRedirect
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
  return render(request, "produto/detail.html", {
    "produto": produto,
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
  })