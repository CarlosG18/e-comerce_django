from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Cliente(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  TYPE = (
      ('pf', 'pessoa fisica'),
      ('em', 'empresa'),
    )
  type_cliente = models.CharField(max_length=2, choices=TYPE, default='pf')
  class Meta:
    abstract = True

class PessoaFisica(Cliente):
  img = models.ImageField(upload_to="cliente/", default="cliente/avatar_default.png")
  cpf_setting = RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
  message="o cpf informado deverá esta no formato 999.999.999-99",
  )
  cpf = models.CharField(max_length=14, validators=[cpf_setting], unique=True)
  total_gasto = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
  total_compras = models.IntegerField(default=0)
  
  def __str__(self):
    return f'username = {self.user.username} password = {self.user.password}'
    
class Empresa(Cliente):
  img = models.ImageField(upload_to="cliente/empresa", default="cliente/avatar_default.png")
  cnpj_setting = RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{7}\-\d{2}$',
  message="o cnpj informado deverá esta no formato XX.XXX.XXX0001-XX",
  )
  cnpj = models.CharField(max_length=18, validators=[cnpj_setting], unique=True)
  segmento = models.CharField(max_length=100)
  total_ganho = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
  total_vendas = models.IntegerField(default=0)

  def __str__(self):
      return f'empresa {self.user.username}'