from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carrinho/', include('carrinho.urls')),
    path('produto/', include('produto.urls')),
    path('cliente/', include('cliente.urls')),
]
