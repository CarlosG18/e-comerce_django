from django.urls import path
from . import views

app_name = "cliente"
urlpatterns = [
  path("", views.index, name="index"),
  path('tipo_cliente/', views.tipocliente, name="tipo-cliente"),
  path('criar_pessoa/', views.criar_pessoa, name="criar_pessoa"),
  path('criar_empresa/', views.criar_empresa, name="criar_empresa"),
  path('perfil/', views.perfil, name="perfil"),
]