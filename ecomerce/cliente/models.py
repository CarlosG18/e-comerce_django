from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

def path_img_client(instance, filename):
  if instance.type_cliente == 'pf':
    return f'cliente/pessoa_fisica/{filename}'
  else:
    return f'cliente/empresa/{filename}'


class Segmento(models.Model):
  nome = models.CharField(max_length=200, null=False, blank=False)

  def __str__(self):
    return self.nome

class Cliente(models.Model):
  TYPE = (
      ('pf', 'pessoa fisica'),
      ('em', 'empresa'),
    )
  
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
  type_cliente = models.CharField(max_length=2, choices=TYPE, default='pf',null=False, blank=False)  
  img = models.ImageField(upload_to=path_img_client, default="cliente/avatar_default.png",null=False, blank=True)

  class Meta:
    abstract = True

class PessoaFisica(Cliente):
  cpf_setting = RegexValidator(
    regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    message="o cpf informado deverá esta no formato 999.999.999-99",
  )

  cpf = models.CharField(max_length=14, validators=[cpf_setting],help_text='formato: 999.999.999-99', unique=True,null=False, blank=False)
  total_gasto = models.DecimalField(max_digits=10,decimal_places=2, default=0.00, null=False, blank=True)
  total_compras = models.IntegerField(default=0,null=False, blank=True)
  
  def __str__(self):
    return self.user.username
    
class Empresa(Cliente):
  cnpj_setting = RegexValidator(
    regex=r'^\d{2}\.\d{3}\.\d{7}\-\d{2}$',
    message="o cnpj informado deverá esta no formato XX.XXX.XXX0001-XX",
  )

  nome_social = models.CharField(max_length=200, null=False, blank=False)
  cnpj = models.CharField(max_length=18, validators=[cnpj_setting],help_text='formato: XX.XXX.XXX0001-XX', unique=True,null=False, blank=False)
  segmento = models.ManyToManyField(to=Segmento,blank=False)
  total_ganho = models.DecimalField(max_digits=10,decimal_places=2, default=0.00,null=False, blank=True)
  total_vendas = models.IntegerField(default=0, null=False, blank=True)

  def __str__(self):
      return self.nome_social