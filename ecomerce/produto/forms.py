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

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['produto'].widget = forms.HiddenInput()

