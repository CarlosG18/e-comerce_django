from django import forms
from .models import Cliente

class FormCriarCliente(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = '__all__'

class FormLogin(forms.ModelForm):
  class Meta:
    model: Cliente
    fields: '__all__'
