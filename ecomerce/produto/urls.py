from django.urls import path
from . import views

app_name = "produto"
urlpatterns = [
  path("", views.ProdutoListView.as_view(), name="index"),
  path("ofertas/", views.ofertas, name="ofertas"),
  path("detail/<int:cod>/", views.detail, name="detail"),
  path("add/", views.add, name="add"),
  path("categoria/<str:cat>/", views.categoria, name="categoria"),
  path("add_fotos/<int:cod>/", views.add_fotos, name="add_fotos"),
  path("remove/<int:cod>/", views.remove, name="remove"),
  path("remove_img/<int:id>/", views.remove_img, name="remove_img"),
]