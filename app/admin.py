from django.contrib import admin
from .models import (
    Profissional, Crianca, Responsavel, Transtorno, Diagnostico,
    Sessao, Alerta, Visualizacao, RelatorioClinico, Usuario
)

# ---------------------
# Inlines
# ---------------------
class DiagnosticoInline(admin.TabularInline):
    model = Diagnostico
    extra = 1

class SessaoInline(admin.TabularInline):
    model = Sessao
    extra = 1

class RelatorioClinicoInline(admin.TabularInline):
    model = RelatorioClinico
    extra = 1

# ---------------------
# Admins
# ---------------------
@admin.register(Crianca)
class CriancaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_nascimento', 'responsavel']  # corrigido data_nascimento -> data_nasc
    search_fields = ['nome', 'responsavel__nome']
    inlines = [
        DiagnosticoInline,
        SessaoInline,
        RelatorioClinicoInline,
    ]

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data_nasc', 'ocupacao', 'user']  # <-- adicionado user
    search_fields = ['nome', 'email', 'ocupacao', 'user__username']  # <-- busca pelo username do User

@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'cpf', 'parentesco', 'sexo', 'cidade', 'user']  # <-- adicionado user
    search_fields = ['nome', 'cpf', 'user__username']  # <-- busca pelo username do User

@admin.register(Transtorno)
class TranstornoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'grau_severidade']
    search_fields = ['nome']

@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ['crianca', 'transtorno', 'profissional', 'data']
    search_fields = ['crianca__nome', 'transtorno__nome', 'profissional__nome']

@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ['crianca', 'profissional', 'data', 'status', 'duracao_minutos']
    search_fields = ['crianca__nome', 'profissional__nome', 'status']

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ['destinatario', 'mensagem', 'data_envio', 'prioridade', 'tipo']  # corrigido responsavel -> destinatario
    search_fields = ['mensagem', 'destinatario__nome']

@admin.register(Visualizacao)
class VisualizacaoAdmin(admin.ModelAdmin):
    list_display = ['alerta', 'responsavel', 'visualizado']
    search_fields = ['alerta__mensagem', 'responsavel__nome']

@admin.register(RelatorioClinico)
class RelatorioClinicoAdmin(admin.ModelAdmin):
    list_display = ['crianca', 'profissional', 'data_geracao']
    search_fields = ['crianca__nome', 'profissional__nome']

# ---------------------
# Ajuste para Usuario
# ---------------------
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['perfil', 'profissional', 'responsavel']
    search_fields = ['perfil', 'profissional__nome', 'responsavel__nome']

