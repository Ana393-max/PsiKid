from django.shortcuts import render
from .models import Crianca, Sessao, Diagnostico, Transtorno, Historico, Responsavel, Alerta, AlertaResponsavel, RelatorioClinico

def profissional(request):
    return render(request, 'profissional.html')

def crianca(request):
    criancas = Crianca.objects.all()
    return render(request, 'crianca.html', {'criancas': criancas})

def diagnostico(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'diagnostico.html', {'diagnosticos': diagnosticos})

def sessao(request):
    sessoes = Sessao.objects.all()
    return render(request, 'sessao.html', {'sessoes': sessoes})

def lista_transtornos(request):
    transtornos = Transtorno.objects.all()
    return render(request, 'transtorno.html', {'transtornos': transtornos})

def historico(request):
    historicos = Historico.objects.all()
    return render(request, 'historico.html', {'historicos': historicos})

def responsavel(request):
    responsaveis = Responsavel.objects.all()
    return render(request, 'responsavel.html', {'responsaveis': responsaveis})

def alerta(request):
    alertas = Alerta.objects.all()
    return render(request, 'alerta.html', {'alertas': alertas})

def alerta_responsavel(request):
    alertas_resp = AlertaResponsavel.objects.all()
    return render(request, 'alerta_responsavel.html', {'alertas_responsavel': alertas_resp})

def relatorio_clinico(request):
    relatorios = RelatorioClinico.objects.all()
    return render(request, 'relatorio_clinico.html', {'relatorios': relatorios})
