from django import forms

class FormProduto(forms.Form):
    nome = forms.CharField(label="nome", max_length=200)
    price = forms.DecimalField(label="price",max_digits=10,decimal_places=2)
    descricao = forms.CharField(label="descricao", max_length=500)
    foto = forms.ImageField(label="foto")