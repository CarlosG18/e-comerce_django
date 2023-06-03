from django import forms
from .models import Cliente

class FormCriarCliente(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
    
  class Meta:
    model = Cliente
    fields = '__all__'