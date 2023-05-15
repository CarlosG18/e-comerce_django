from django.db import models
from cliente.models import Cliente
from produto.models import Produto

class Carrinho(models.Model):
  cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'carrinho do cliente {self.cliente.nome}'
  
class ItemCarrinho(models.Model):
  carrinho = models.ForeignKey(Carrinho,on_delete=models.CASCADE)
  produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
  
  def __str__(self):
    return f' item {self.produto.nome} do carinho do cliente {self.carrinho.cliente.nome}'

