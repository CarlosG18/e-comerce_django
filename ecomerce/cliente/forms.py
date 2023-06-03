from django import forms
from .models import UserPessoaFisica, UserEmpresa

class FormUserPessoaFisica(forms.ModelForm):
  class Meta:
    model = UserPessoaFisica
    fields = '__all__'
    
class FormUserEmpresa(forms.ModelForm):
  class Meta:
    model = UserEmpresa
    fields = '__all__'