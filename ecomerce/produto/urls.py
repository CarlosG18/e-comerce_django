from django.urls import path
from . import views

app_name = "produto"
urlpatterns = [
  path("", views.index, name="index"),
  path("ofertas/", views.ofertas, name="ofertas"),
]