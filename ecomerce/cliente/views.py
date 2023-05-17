from django.shortcuts import render
from .models import Cliente

def index(request):
  clientes = Cliente.objects.all()
  return render(request, "cliente/index.html", {
    "clientes": clientes,
  })

def login(request):
  return render(request, "cliente/login.html")
