from django.urls import path
from . import views

app_name = "cliente"
urlpatterns = [
  path("", views.index, name="index"),
  #path("criar_conta/", views.criar_conta, name="criar_conta"),
  path('tipo_cliente/', views.tipocliente, name="tipo-cliente"),
  path('criar_pessoa/', views.criar_pessoa, name="criar_pessoa"),
  path('criar_empresa/', views.criar_empresa, name="criar_empresa"),
  path('login/', views.login, name="login"),
  # path('perfil/<int:id>/', views.perfil, name="perfil"),
]