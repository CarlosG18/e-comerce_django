from django.shortcuts import render
from .models import Produto, ListImages

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