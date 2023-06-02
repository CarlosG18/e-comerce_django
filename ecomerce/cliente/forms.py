from django import forms
from .models import Cliente
from django.contrib.auth.models import User

class UserClienteForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    #cpf = forms.CharField(max_length=14)

    def save(self):
      user = User.objects.create_user(
        username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password'])
      user.save()

        # Cria uma nova instância de Cliente com base nos dados do formulário
      cliente = Cliente(user=user)
      cliente.save()


"""
class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ('username','password')

class FormCriarCliente(forms.ModelForm):
  user_form = UserForm()
  class Meta:
    model = Cliente
    fields = '__all__'
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['user'].widget = forms.HiddenInput()
    self.fields.update(self.user_form.fields)
  """