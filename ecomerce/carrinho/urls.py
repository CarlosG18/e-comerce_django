from django.urls import path
from . import views

app_name = "carrinho"
urlpatterns = [
  path("", views.index, name="index"),
  path("create/", views.create, name="create"),
  path("delete/<int:id>", views.delete, name="delete"),
  path("add_item/<int:cod>", views.add_item, name="add_item"),
  path("remove_item/<int:cod>/", views.remove_item, name="remove_item"),
]