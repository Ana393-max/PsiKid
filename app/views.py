from django.shortcuts import render
from .models import (
    Crianca, Sessao, Diagnostico, Transtorno,
    Responsavel, Profissional,
    Alerta, Consulta, Visualizacao, RelatorioClinico
)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):  # view para login
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # se seu User usa username, tem que autenticar com username:
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')  # redireciona após login
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
    return render(request, 'login.html')
# -------------------------
# Página inicial do profissional
# -------------------------
def profissional(request):
    profissionais = Profissional.objects.all()  # passa os profissionais para o template
    return render(request, 'profissional.html', {'profissionais': profissionais})


# -------------------------
# RF03 - Lista de crianças
# -------------------------
def crianca(request):
    criancas = Crianca.objects.all()
    return render(request, 'crianca.html', {'criancas': criancas})


# -------------------------
# RF06 - Diagnósticos
# -------------------------
def diagnostico(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'diagnostico.html', {'diagnosticos': diagnosticos})


# -------------------------
# RF07 - Sessões
# -------------------------
def sessao(request):
    sessoes = Sessao.objects.all()
    return render(request, 'sessao.html', {'sessoes': sessoes})


# -------------------------
# RF05 - Tipos de transtornos
# -------------------------
def lista_transtornos(request):
    transtornos = Transtorno.objects.all()
    return render(request, 'transtorno.html', {'transtornos': transtornos})


# -------------------------
# RF03 - Responsáveis
# -------------------------
def responsavel(request):
    responsaveis = Responsavel.objects.all()
    return render(request, 'responsavel.html', {'responsaveis': responsaveis})


# -------------------------
# RF08 - Alertas
# -------------------------
def alerta(request):
    alertas = Alerta.objects.all()
    return render(request, 'alerta.html', {'alertas': alertas})


# -------------------------
# RF10 - Visualização de alertas
# -------------------------
def visualizacao_alertas(request):
    visualizacoes = Visualizacao.objects.all()
    return render(request, 'visualizacao.html', {'visualizacoes': visualizacoes})


# -------------------------
# RF09 - Histórico (Consulta)
# -------------------------
def historico(request):
    consultas = Consulta.objects.all()
    return render(request, 'historico.html', {'consultas': consultas})


# -------------------------
# RF11 - Relatórios Clínicos
# -------------------------
def relatorio_clinico(request):
    relatorios = RelatorioClinico.objects.all()
    return render(request, 'relatorio_clinico.html', {'relatorios': relatorios})
