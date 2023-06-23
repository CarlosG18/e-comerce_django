from django import forms
from .models import Produto, ListImages, Comentario

class FormProduto(forms.ModelForm):
    class Meta:
      model = Produto
      exclude = ['loja', 'media_stars']
      
      widgets = {
            'descricao': forms.Textarea(attrs={'class': 'text-area'}),
            'status': forms.Select(attrs={'class': 'status'}),
            'categoria': forms.Select(attrs={'class': 'status'}),
        }

class FormImages(forms.ModelForm):
  class Meta:
    model = ListImages
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['produto'].widget = forms.HiddenInput()
    
class FormComentario(forms.ModelForm):
  class Meta:
    model = Comentario
    #fields = '__all__'
    exclude = ['produto', 'cliente']

