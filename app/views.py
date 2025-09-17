from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import (
    Crianca, Sessao, Diagnostico, Transtorno,
    Responsavel, Profissional,
    Alerta, Consulta, Visualizacao, RelatorioClinico
)

# -------------------------
# View para login
# -------------------------
def index(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')  # campo do form deve ser 'cpf'
        senha = request.POST.get('senha')

        user = authenticate(request, username=cpf, password=senha)
        if user is not None:
            login(request, user)
            # Descobre se o user é responsável ou profissional
            if hasattr(user, 'responsavel'):
                return redirect('responsavel')
            elif hasattr(user, 'profissional'):
                return redirect('profissional')
            else:
                messages.warning(request, 'Seu usuário não tem perfil definido.')
                return redirect('index')  # corrigido aqui
        else:
            messages.error(request, 'CPF ou senha inválidos.')
    return render(request, 'index.html')


# -------------------------
# Página inicial do profissional
# -------------------------
@login_required
def profissional(request):
    """Página inicial do profissional"""
    profissionais = Profissional.objects.all()
    return render(request, 'profissional.html', {'profissionais': profissionais})


# -------------------------
# Página inicial do responsável
# -------------------------
@login_required
def responsavel(request):
    """Página inicial do responsável"""
    responsaveis = Responsavel.objects.all()
    return render(request, 'responsavel.html', {'responsaveis': responsaveis})


# -------------------------
# RF03 - Lista de crianças
# -------------------------
@login_required
def crianca(request):
    criancas = Crianca.objects.all()
    return render(request, 'crianca.html', {'criancas': criancas})


# -------------------------
# RF06 - Diagnósticos
# -------------------------
@login_required
def diagnostico(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'diagnostico.html', {'diagnosticos': diagnosticos})


# -------------------------
# RF07 - Sessões
# -------------------------
@login_required
def sessao(request):
    sessoes = Sessao.objects.all()
    return render(request, 'sessao.html', {'sessoes': sessoes})


# -------------------------
# RF05 - Tipos de transtornos
# -------------------------
@login_required
def lista_transtornos(request):
    transtornos = Transtorno.objects.all()
    return render(request, 'transtorno.html', {'transtornos': transtornos})


# -------------------------
# RF08 - Alertas
# -------------------------
@login_required
def alerta(request):
    alertas = Alerta.objects.all()
    return render(request, 'alerta.html', {'alertas': alertas})


# -------------------------
# RF10 - Visualização de alertas
# -------------------------
@login_required
def visualizacao_alertas(request):
    visualizacoes = Visualizacao.objects.all()
    return render(request, 'visualizacao.html', {'visualizacoes': visualizacoes})


# -------------------------
# RF09 - Histórico (Consulta)
# -------------------------
@login_required
def historico(request):
    consultas = Consulta.objects.all()
    return render(request, 'historico.html', {'consultas': consultas})


# -------------------------
# RF11 - Relatórios Clínicos
# -------------------------
@login_required
def relatorio_clinico(request):
    relatorios = RelatorioClinico.objects.all()
    return render(request, 'relatorio_clinico.html', {'relatorios': relatorios})
