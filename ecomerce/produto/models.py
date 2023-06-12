from distutils.command.upload import upload
from email.policy import default
from django.db import models
from cliente.models import PessoaFisica, Empresa
import os

"""
def caminho_personalizado(instance, filename):
  path_name = f"produto_{instance.produto.nome}"
  caminho = os.path.join("produto/", path_name)
  return os.path.join(caminho, filename)
"""

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
      return self.nome

class Produto(models.Model):
  codigo = models.IntegerField(primary_key=True)
  nome = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  descricao = models.TextField()
  quantidade = models.IntegerField(default=0)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
  foto = models.ImageField(upload_to="produto/", default="produto/produto_default.png")
  media_stars = models.DecimalField(max_digits=3, decimal_places=2,default=0)
  loja = models.ForeignKey(Empresa,on_delete=models.CASCADE)
  
  STATUS = (
      ("o", "oferta"),
      ("f", "falta"),
      ("n", "normal"),
    )
  
  status = models.CharField(max_length=1,choices=STATUS,default='n',help_text="status do produto")
  
  def __str__(self):
    return f' produto {self.nome}'
  

class ListImages(models.Model):
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  foto = models.ImageField(upload_to="produto/", default="produto/produto_default.png")
  
  def __str__(self):
    return f'imagem do produto {self.produto.nome}'
    
class Comentario(models.Model):
  cliente = models.ForeignKey(PessoaFisica,on_delete=models.CASCADE)
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  comentario = models.TextField()
  
  STARS = (
      (1,"péssimo"),
      (2,"mediano"),
      (3,"ótimo"),
      (4,"excelente"),
      (5,"fantástico")
    )
  
  stars = models.IntegerField(choices=STARS)
  
  def __str__(self):
    return f'comentario da cliente {self.cliente.nome} sobre o produto {self.produto.nome}'