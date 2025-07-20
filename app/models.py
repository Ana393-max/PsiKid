from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

class Crianca(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    responsavel = models.ForeignKey('Responsavel', on_delete=models.CASCADE, related_name='criancas')

    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Transtorno(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Diagnostico(models.Model):
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    transtorno = models.ForeignKey(Transtorno, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Diagnóstico de {self.crianca.nome} por {self.profissional.nome}"

class Sessao(models.Model):
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    anotacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Agendada','Agendada'), ('Realizada','Realizada'), ('Cancelada','Cancelada')])
    duracao_minutos = models.PositiveIntegerField()

    def __str__(self):
        return f"Sessão em {self.data} com {self.crianca.nome}"
    
class Historico(models.Model):
    crianca = models.ForeignKey('Crianca', on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Histórico de {self.crianca.nome} - {self.data}"

class Alerta(models.Model):
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class AlertaResponsavel(models.Model):
    alerta = models.ForeignKey(Alerta, on_delete=models.CASCADE)
    responsavel = models.ForeignKey('Responsavel', on_delete=models.CASCADE)
    visualizado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.alerta.titulo} - {self.responsavel.nome}"

class RelatorioClinico(models.Model):
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Relatório Clínico de {self.crianca.nome} - {self.data}"

