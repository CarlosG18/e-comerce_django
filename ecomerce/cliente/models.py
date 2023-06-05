from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class PessoaFisica(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.ImageField(upload_to="cliente/", default="cliente/avatar_default.png")
  cpf_setting = RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
  message="o cpf informado deverá esta no formato 999.999.999-99",
  )
  cpf = models.CharField(max_length=14, validators=[cpf_setting], unique=True)
  
  def __str__(self):
    return f'username = {self.user.username} password = {self.user.password}'
    
class Empresa(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  logo = models.ImageField(upload_to="cliente/empresa", default="cliente/avatar_default.png")
  cnpj_setting = RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}\d{4}-d{2}$',
  message="o cpf informado deverá esta no formato XX.XXX.XXX0001-XX",
  )
  cnpj = models.CharField(max_length=18, validators=[cnpj_setting], unique=True)
  segmento = models.CharField(max_length=100)

  def __str__(self):
      return f'empresa {self.user.username}'