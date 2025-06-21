from django.shortcuts import render
from django.views import View
from .models import Responsavel, Transtorno, Crianca, Diagnostico, Sessao, Alerta

class IndexView(View):
    def get(self, request, *args, **kwargs):
        #criancas = Crianca.objects.select_related('responsavel').all()
        #return render(request, 'index.html', {'criancas': criancas})
        return render(request, 'index.html')

class ResponsaveisView(View):
    def get(self, request, *args, **kwargs):
        # Removido select_related('cidade') pois cidade é CharField
        responsaveis = Responsavel.objects.all()
        return render(request, 'responsavel.html', {'responsaveis': responsaveis})

class TranstornosView(View):
    def get(self, request, *args, **kwargs):
        transtornos = Transtorno.objects.all()
        return render(request, 'transtorno.html', {'transtornos': transtornos})

class CriancasView(View):
    def get(self, request, *args, **kwargs):
        criancas = Crianca.objects.select_related('responsavel').all()
        return render(request, 'crianca.html', {'criancas': criancas})

class DiagnosticosView(View):
    def get(self, request, *args, **kwargs):
        diagnosticos = Diagnostico.objects.select_related('crianca', 'transtorno', 'profissional').all()
        return render(request, 'diagnostico.html', {'diagnosticos': diagnosticos})

class SessoesView(View):
    def get(self, request, *args, **kwargs):
        sessoes = Sessao.objects.select_related('crianca', 'profissional').all()
        return render(request, 'sessao.html', {'sessoes': sessoes})

class AlertasView(View):
    def get(self, request, *args, **kwargs):
        # Remove select_related('crianca') pois Alerta não tem FK para crianca
        alertas = Alerta.objects.select_related('destinatario').all()
        return render(request, 'alerta.html', {'alertas': alertas})

# RF08 - Histórico de atendimentos da criança
class HistoricoView(View):
    def get(self, request, *args, **kwargs):
        criancas = Crianca.objects.prefetch_related('sessoes', 'diagnosticos').all()
        return render(request, 'historico.html', {'criancas': criancas})

# RF09 - Alertas recebidos (visualização para responsáveis)
class AlertasResponsavelView(View):
    def get(self, request, *args, **kwargs):
        # Remove select_related('crianca')
        alertas = Alerta.objects.select_related('destinatario').all()
        return render(request, 'alerta_responsavel_list.html', {'alertas': alertas})

# Nova view para o Dashboard do Profissional (página de design)
class ProfissionalDashboardView(View):
    def get(self, request, *args, **kwargs):
        # Renderiza apenas o template da dashboard do profissional
        return render(request, 'profissional.html')
