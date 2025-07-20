from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rotas das páginas personalizadas
    path('profissionais/', views.profissional, name='profissional'),
    path('criancas/', views.crianca, name='criancas'), 
    path('diagnosticos/', views.diagnostico, name='diagnosticos'),
    path('sessoes/', views.sessao, name='sessoes'),
    path('transtornos/', views.lista_transtornos, name='lista_transtornos'),
    path('historicos/', views.historico, name='historicos'),
    path('responsaveis/', views.responsavel, name='responsaveis'),
    path('alertas/', views.alerta, name='alertas'),
    path('alertas-responsavel/', views.alerta_responsavel, name='alertas_responsavel'),
    path('relatorios-clinicos/', views.relatorio_clinico, name='relatorios_clinicos'),
]
