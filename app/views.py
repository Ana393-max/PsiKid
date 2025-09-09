from django.shortcuts import render
from .models import (
    Crianca, Sessao, Diagnostico, Transtorno,
    Responsavel, Profissional, Ocupacao,
    Alerta, Consulta, Visualizacao, RelatorioClinico
)

# Página inicial do profissional
def profissional(request):
    return render(request, 'profissional.html')


# RF03 - Lista de crianças
def crianca(request):
    criancas = Crianca.objects.all()
    return render(request, 'crianca.html', {'criancas': criancas})


# RF06 - Diagnósticos
def diagnostico(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'diagnostico.html', {'diagnosticos': diagnosticos})


# RF07 - Sessões
def sessao(request):
    sessoes = Sessao.objects.all()
    return render(request, 'sessao.html', {'sessoes': sessoes})


# RF05 - Tipos de transtornos
def lista_transtornos(request):
    transtornos = Transtorno.objects.all()
    return render(request, 'transtorno.html', {'transtornos': transtornos})


# RF03 - Responsáveis
def responsavel(request):
    responsaveis = Responsavel.objects.all()
    return render(request, 'responsavel.html', {'responsaveis': responsaveis})


# RF08 - Alertas
def alerta(request):
    alertas = Alerta.objects.all()
    return render(request, 'alerta.html', {'alertas': alertas})


# RF10 - Visualização de alertas
def visualizacao_alertas(request):
    visualizacoes = Visualizacao.objects.all()
    return render(request, 'visualizacao.html', {'visualizacoes': visualizacoes})


# RF09 - Histórico (Consulta)
def consulta(request):
    consultas = Consulta.objects.all()
    return render(request, 'consulta.html', {'consultas': consultas})


# RF11 - Relatórios Clínicos
def relatorio_clinico(request):
    relatorios = RelatorioClinico.objects.all()
    return render(request, 'relatorio_clinico.html', {'relatorios': relatorios})
