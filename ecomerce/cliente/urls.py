from django.urls import path
from . import views

app_name = "cliente"
urlpatterns = [
  path("", views.index, name="index"),
  path("criar_conta/", views.criar_conta, name="criar_conta"),
  path('perfil/<int:id>/', views.perfil, name="perfil"),
]