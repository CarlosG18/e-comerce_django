from django.urls import path
from . import views

app_name = "produto"
urlpatterns = [
  path("", views.ProdutoListView.as_view(), name="index"),
  path("detail/<int:cod>/", views.detail, name="detail"),
  path("add/", views.add, name="add"),
  path("categoria/<str:cat>/", views.categoria, name="categoria"),
  path("add_fotos/<int:cod>/", views.add_fotos, name="add_fotos"),
  path("remove/<int:cod>/", views.remove, name="remove"),
  path("remove_img/<int:id>/", views.remove_img, name="remove_img"),
  path("remove_comentario/<int:id>/<int:cod>/", views.remove_comentario, name="remove_comentario"),
  path("produtos_emp/", views.produtos_emp, name="produtos_emp"),
  path("estoque/", views.estoque, name="estoque"),
  path("estoque/upgrade/<int:cod>", views.estoque_up, name='estoque_up'),
]