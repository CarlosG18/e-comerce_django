from django import forms
from django.contrib.auth.models import User
from .models import PessoaFisica, Empresa

class FormUser(forms.ModelForm):
  class Meta:
    model = User
    fields = ("username", "email", "password")

class FormPessoaFisica(forms.ModelForm):
  class Meta:
    model = PessoaFisica
    exclude = ['user']


    widgets = {
      'type_cliente': forms.Select(attrs={'class': 'type_cli'})
    }
    
class FormEmpresa(forms.ModelForm):
  class Meta:
    model = Empresa
    exclude = ['user']

    widgets = {
      'type_cliente': forms.Select(attrs={'class': 'type_cli'})
    }