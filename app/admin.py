from django.contrib import admin
from .models import (
    Profissional, Crianca, Responsavel, Transtorno, Diagnostico,
    Sessao, Historico, Alerta, AlertaResponsavel, RelatorioClinico
)

class DiagnosticoInline(admin.TabularInline):
    model = Diagnostico
    extra = 1

class SessaoInline(admin.TabularInline):
    model = Sessao
    extra = 1

class HistoricoInline(admin.TabularInline):
    model = Historico
    extra = 1

class RelatorioClinicoInline(admin.TabularInline):
    model = RelatorioClinico
    extra = 1

@admin.register(Crianca)
class CriancaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_nascimento', 'responsavel']
    search_fields = ['nome', 'responsavel__nome']
    inlines = [
        DiagnosticoInline,
        SessaoInline,
        HistoricoInline,
        RelatorioClinicoInline,
    ]

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data_nascimento']
    search_fields = ['nome', 'email']

@admin.register(Transtorno)
class TranstornoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
    search_fields = ['nome']

@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ['crianca', 'transtorno', 'profissional', 'data']
    search_fields = ['crianca__nome', 'transtorno__nome', 'profissional__nome']

@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ['crianca', 'profissional', 'data', 'status', 'duracao_minutos']
    search_fields = ['crianca__nome', 'profissional__nome', 'status']

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ['crianca', 'data', 'descricao']
    search_fields = ['crianca__nome']

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'responsavel', 'data_criacao']
    search_fields = ['titulo', 'responsavel__nome']

@admin.register(RelatorioClinico)
class RelatorioClinicoAdmin(admin.ModelAdmin):
    list_display = ['crianca', 'data', 'descricao']
    search_fields = ['crianca__nome', 'descricao']
