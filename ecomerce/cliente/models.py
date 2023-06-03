from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class UserPessoaFisica(AbstractUser):
  class Meta:
    verbose_name = 'pessoa física'
    verbose_name_plural = 'pessoas físicas'
    
  groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='grupos',
        blank=True,
        help_text='Os grupos aos quais a pessoa física pertence.',
        related_name='user_pessoafisica_set',
        related_query_name='user_pessoafisica'
    )
  user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='permissões',
        blank=True,
        help_text='Permissões específicas para a pessoa física.',
        related_name='user_pessoafisica_set',
        related_query_name='user_pessoafisica'
  )

  avatar = models.ImageField(upload_to="cliente/", default="cliente/avatar_default.png")
  cpf_setting = RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
  message="o cpf informado deverá esta no formato 999.999.999-99",
  )
  cpf = models.CharField(max_length=14, validators=[cpf_setting], unique=True)
  
  def __str__(self):
    return f'cliente {self.username}'

class UserEmpresa(AbstractUser):
  class Meta:
    verbose_name = 'empresa'
    verbose_name_plural = 'empresas'
    
  groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='grupos',
        blank=True,
        help_text='Os grupos aos quais a empresa pertence.',
        related_name='user_empresa_set',
        related_query_name='user_empresa'
    )
  user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='permissões',
        blank=True,
        help_text='Permissões específicas para a empresa.',
        related_name='user_empresa_set',
        related_query_name='user_empresa'
  )
    
  logo = models.ImageField(upload_to="cliente/empresa", default="cliente/avatar_default.png")
  cnpj_setting = RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-d{2}$',
  message="o cpf informado deverá esta no formato XX.XXX.XXX/0001-XX",
  )
  cnpj = models.CharField(max_length=18, validators=[cnpj_setting], unique=True)
  segmento = models.CharField(max_length=100)