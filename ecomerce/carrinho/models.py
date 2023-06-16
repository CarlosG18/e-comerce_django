from django.db import models
from produto.models import Produto
from cliente.models import PessoaFisica

class Carrinho(models.Model):
  nome = models.CharField(max_length=200, default="carrinho_default")
  cliente = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE)
  qtd_produtos = models.IntegerField(default=0)
  preco_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
  

  def __str__(self):
    return f'carrinho do cliente {self.cliente.user.username}'
  
class ItemCarrinho(models.Model):
  carrinho = models.ForeignKey(Carrinho,on_delete=models.CASCADE, null=True)
  produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
  quantidade = models.IntegerField(default=1)
  preco_acumulado = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
  
  def __str__(self):
    return f' carrinho = {self.carrinho} - produto = {self.produto}'

