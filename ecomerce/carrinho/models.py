from django.db import models
from produto.models import Produto
from cliente.models import PessoaFisica

class Carrinho(models.Model):
  nome = models.CharField(max_length=200, default="carrinho_default")
  cliente = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE)
  qtd_produtos = models.IntegerField(default=0)
  preco_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
  close_car = models.BooleanField(default=False)
  

  def __str__(self):
    return f'carrinho do cliente {self.cliente.user.username}'
  
class ItemCarrinho(models.Model):
  carrinho = models.ForeignKey(Carrinho,on_delete=models.CASCADE, null=True)
  produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
  quantidade = models.IntegerField(default=1)
  preco_acumulado = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
  
  def __str__(self):
    return f' carrinho = {self.carrinho} - produto = {self.produto}'
    
class Compra(models.Model):
  carrinho = models.ForeignKey(Carrinho,on_delete=models.CASCADE)
  STATUS = (
      ('ss', 'sem status'),
      ('pp', 'pagamento pedente'),
      ('ec', 'produto à caminho'),
      ('se', 'saiu para entrega'),
      ('re', 'produto recebido'),
    )
  
  status = models.CharField(max_length=2,choices=STATUS, default='ss')
  data = models.DateField()
  
  def __str__(self):
    return f'compra do cliente = {self.carrinho.cliente.user.username} R$ = {self.carrinho.preco_total}'

