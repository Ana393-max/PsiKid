from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Raiz do site exibe o formulário de login
    path('', views.index, name='index'),  # <-- essa é a alteração principal

    # Rotas das páginas personalizadas
    path('profissional/', views.profissional, name='profissional'),
    path('criancas/', views.crianca, name='criancas'),
    path('diagnosticos/', views.diagnostico, name='diagnosticos'),
    path('sessoes/', views.sessao, name='sessoes'),
    path('transtornos/', views.lista_transtornos, name='lista_transtornos'),
    path('historicos/', views.historico, name='historicos'),  # agora está certo!
    path('responsavel/', views.responsavel, name='responsavel'),
    path('responsavel/alertas/', views.alertas_responsavel, name='alertas_responsavel'),
    path('responsavel/historico/', views.historico_responsavel, name='historico_responsavel'),
    path('alertas/', views.alerta, name='alertas'),
    path('visualizacoes/', views.visualizacao_alertas, name='visualizacoes'),
    path('relatorios-clinicos/', views.relatorio_clinico, name='relatorios_clinicos'),
]
