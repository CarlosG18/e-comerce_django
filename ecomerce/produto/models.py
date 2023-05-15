from django.db import models

class Produto(models.Model):
  codigo = models.IntegerField(primary_key=True)
  nome = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  descricao = models.TextField()
  
  def __str__(self):
    return f' produto {self.nome}'