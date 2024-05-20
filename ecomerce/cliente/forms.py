from django import forms
from django.contrib.auth.models import User
from .models import PessoaFisica, Empresa

# definido o type_cliente do model Pessoa Fisica como padrão: 'pf' e não editavel
class PessoaFisicaAdminForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PessoaFisicaAdminForm, self).__init__(*args, **kwargs)
        # Define o valor padrão e torna o campo não editável
        self.fields['type_cliente'].initial = 'pf'
        self.fields['type_cliente'].disabled = True

# definido o type_cliente do model Empresa como padrão: 'em' e não editavel
class EmpresaAdminForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmpresaAdminForm, self).__init__(*args, **kwargs)
        # Define o valor padrão e torna o campo não editável
        self.fields['type_cliente'].initial = 'em'
        self.fields['type_cliente'].disabled = True

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