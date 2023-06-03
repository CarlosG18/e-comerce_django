from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Cliente(models.Model):
  username = models.CharField(max_length=200)
  email = models.EmailField()
  password = models.CharField(max_length=180)
  avatar = models.ImageField(upload_to="cliente/", default="cliente/avatar_default.png")
  cpf_setting = RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
   message="o cpf informado deverá esta no formato 999.999.999-99",
  )
  cpf = models.CharField(max_length=14, validators=[cpf_setting], unique=True)
  TYPE = (
      ("f", "pessoa-fisica"),
      ("e", "empresa"),
    )
  type_cliente = models.CharField(max_length=1, choices=TYPE, help_text="tipo de cliente", default='f')
  
  def __str__(self):
    return f'cliente {self.username}'