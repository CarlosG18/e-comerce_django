from django import forms
from .models import Produto, ListImages

class FormProduto(forms.ModelForm):
    class Meta:
      model = Produto
      fields = '__all__'

class FormImages(forms.ModelForm):
  class Meta:
    model = ListImages
    fields = '__all__'