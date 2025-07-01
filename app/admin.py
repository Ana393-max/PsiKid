from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from .models import Responsavel, Crianca, Transtorno, Diagnostico, Sessao, Alerta, Perfil

# Inline para mostrar o perfil extendido Usuario junto ao User padrão
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil do Usuário'

# Custom UserAdmin para adicionar o inline Perfil
class UserAdmin(DjangoUserAdmin):
    inlines = (PerfilInline,)

# Registrar o User padrão com o UserAdmin customizado
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Registrar o modelo Perfil separadamente (opcional)
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['user', 'tipo']
    list_filter = ['tipo']
    search_fields = ['user__username', 'tipo']
# Demais modelos (sem Cidade, ajustado conforme revisão anterior)
@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone', 'email', 'parentesco', 'cidade']
    search_fields = ['nome', 'cpf', 'email']
    list_filter = ['cidade', 'parentesco']

@admin.register(Crianca)
class CriancaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_nascimento', 'responsavel', 'data_cadastro']
    search_fields = ['nome']
    list_filter = ['responsavel']
    filter_horizontal = ['transtornos']

@admin.register(Transtorno)
class TranstornoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'grau_severidade']
    search_fields = ['nome']
    list_filter = ['grau_severidade']

@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ['crianca', 'transtorno', 'profissional', 'data']
    list_filter = ['transtorno', 'profissional']
    search_fields = ['crianca__nome']

@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ['crianca', 'profissional', 'data', 'status', 'duracao_minutos']
    list_filter = ['status', 'profissional']
    search_fields = ['crianca__nome']

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ['destinatario', 'tipo', 'prioridade', 'data_envio']
    list_filter = ['tipo', 'prioridade']
    search_fields = ['destinatario__nome']
