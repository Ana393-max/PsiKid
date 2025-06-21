from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import (
    IndexView,
    ResponsaveisView,
    TranstornosView,
    CriancasView,
    DiagnosticosView,
    SessoesView,
    AlertasView,
    ProfissionalDashboardView,  # Import da nova view
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # RF01 - Autenticação (visual por enquanto)
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),

    # Página inicial
    path('', IndexView.as_view(), name='index'),

    # RF02 - Crianças
    path('criancas/', CriancasView.as_view(), name='criancas'),

    # RF03 - Responsáveis
    path('responsaveis/', ResponsaveisView.as_view(), name='responsaveis'),

    # RF04 - Transtornos
    path('transtornos/', TranstornosView.as_view(), name='transtornos'),

    # RF05 - Diagnósticos
    path('diagnosticos/', DiagnosticosView.as_view(), name='diagnosticos'),

    # RF06 - Sessões de Atendimento
    path('sessoes/', SessoesView.as_view(), name='sessoes'),

    # RF07 - Alertas (profissional)
    path('alertas/', AlertasView.as_view(), name='alertas'),

    # RF08 - Histórico de atendimento (responsável ou profissional)
    path('historico/', TemplateView.as_view(template_name='historico.html'), name='historico'),

    # RF09 - Alertas recebidos (responsável)
    path('meus-alertas/', TemplateView.as_view(template_name='alerta_responsavel_list.html'), name='meus_alertas'),

    # Nova rota para o dashboard do profissional (design da página)
    path('profissional/', ProfissionalDashboardView.as_view(), name='profissional_dashboard'),
]
