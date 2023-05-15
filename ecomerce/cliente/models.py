from django.db import models
from django.core.validators import RegexValidator


class Cliente(models.Model):
  nome = models.CharField(max_length=200)
  email = models.EmailField(help_text="insira seu email")

  cpf_setting = RegexValidator(
    regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    message="o cpf informado deverá esta no formato 999.999.999-99",
  )

  cpf = models.CharField(primary_key=True, max_length=14, validators=[cpf_setting], unique=True)
  
  def __str__(self):
    return f'cliente {self.nome}'