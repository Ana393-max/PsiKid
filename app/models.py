from django.db import models
from django.contrib.auth.models import User

# RF01 – Extensão de autenticação do usuário
class Usuario(models.Model):
    PERFIS = [
        ('Profissional', 'Profissional'),
        ('Responsavel', 'Responsável'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil = models.CharField(max_length=20, choices=PERFIS)
    # Relacionamento genérico com pessoa (Responsável ou Profissional)
    # Pode ser usado se você quiser fazer herança ou polimorfismo
    # pessoa = models.ForeignKey('Pessoa', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.perfil})"


# RF03 – Responsável
class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20, null=True, blank=True)
    parentesco = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome


# RF02 – Criança
class Crianca(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    historico_situacao = models.TextField(null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, related_name='criancas')
    # Relacionamento M:N com transtornos via ManyToManyField
    transtornos = models.ManyToManyField('Transtorno', blank=True)

    def __str__(self):
        return self.nome


# RF04 – Transtorno
class Transtorno(models.Model):
    GRAUS = [
        ('Leve', 'Leve'),
        ('Moderado', 'Moderado'),
        ('Grave', 'Grave'),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    grau_severidade = models.CharField(max_length=10, choices=GRAUS)

    def __str__(self):
        return self.nome


# RF05 – Diagnóstico
class Diagnostico(models.Model):
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE, related_name='diagnosticos')
    transtorno = models.ForeignKey(Transtorno, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Usuario, limit_choices_to={'perfil': 'Profissional'}, on_delete=models.SET_NULL, null=True)
    data = models.DateField()
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Diagnóstico de {self.crianca} - {self.transtorno}"


# RF06 – Sessão de Atendimento
class Sessao(models.Model):
    STATUS = [
        ('Agendada', 'Agendada'),
        ('Realizada', 'Realizada'),
        ('Cancelada', 'Cancelada'),
    ]
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE, related_name='sessoes')
    profissional = models.ForeignKey(Usuario, limit_choices_to={'perfil': 'Profissional'}, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField()
    anotacoes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    duracao_minutos = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Sessão {self.data} - {self.crianca}"


# RF07 – Alerta
class Alerta(models.Model):
    PRIORIDADES = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    ]
    TIPOS = [
        ('Lembrete', 'Lembrete'),
        ('Emergência', 'Emergência'),
        ('Atraso', 'Atraso'),
    ]
    destinatario = models.ForeignKey(Responsavel, on_delete=models.CASCADE, related_name='alertas')
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES)
    tipo = models.CharField(max_length=15, choices=TIPOS)

    def __str__(self):
        return f"Alerta para {self.destinatario} - {self.tipo}"


# RF09 – Visualizacao dos alertas (pode ser um modelo para controle, ou uma view)
class Visualizacao(models.Model):
    alerta = models.ForeignKey(Alerta, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    data_visualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('alerta', 'responsavel')

    def __str__(self):
        return f"Visualização do alerta {self.alerta.id} por {self.responsavel.nome}"
