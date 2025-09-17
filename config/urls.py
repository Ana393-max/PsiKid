from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Raiz do site exibe o formulário de login
    path('', views.index, name='index'),  # <-- essa é a alteração principal

    # Rotas das páginas personalizadas
    path('profissionais/', views.profissional, name='profissionais'),
    path('criancas/', views.crianca, name='criancas'),
    path('diagnosticos/', views.diagnostico, name='diagnosticos'),
    path('sessoes/', views.sessao, name='sessoes'),
    path('transtornos/', views.lista_transtornos, name='lista_transtornos'),
    path('historicos/', views.historico, name='historicos'),  # agora está certo!
    path('responsaveis/', views.responsavel, name='responsaveis'),
    path('alertas/', views.alerta, name='alertas'),
    path('visualizacoes/', views.visualizacao_alertas, name='visualizacoes'),
    path('relatorios-clinicos/', views.relatorio_clinico, name='relatorios_clinicos'),
]
