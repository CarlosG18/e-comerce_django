from django.db import models

class Cliente(models.Model):
  nome = models.CharField(max_length=200)
  email = models.EmailField(help_text="insira seu email")
  cpf = models.IntegerField(primary_key=True)
  
  def __str__(self):
    return f'cliente {self.nome}'