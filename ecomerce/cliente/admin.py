from django.contrib import admin
from .models import PessoaFisica, Empresa, Segmento
from .forms import PessoaFisicaAdminForm, EmpresaAdminForm

# Registrando o modelo Pessoa Fisica no site do Admin
@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf']
    search_fields = ('nome',)
    list_filter = ('total_gasto','total_compras',)
    list_per_page = 5
    form = PessoaFisicaAdminForm

# Registrando o modelo Empresa no site do Admin
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['user','nome_social','cnpj']
    list_per_page = 5
    list_filter = ('segmento','total_ganho','total_vendas',)
    search_fields = ('nome_social',)
    form = EmpresaAdminForm

# Registrando o modelo Segmeto no site do Admin
@admin.register(Segmento)
class SegmentoAdmin(admin.ModelAdmin):
    pass
