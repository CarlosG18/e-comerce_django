from django.urls import path
from . import views

app_name = "cliente"
urlpatterns = [
  path("", views.index, name="index"),
  path("login/", views.login, name="login"),
  path("criar_conta/", views.criar_conta, name="criar_conta"),
]