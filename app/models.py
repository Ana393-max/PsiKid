from django.db import models

# -------------------------
# RF03 - Pessoa (classe base)
# -------------------------
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

# -------------------------
# RF03 - Responsável (herda de Pessoa)
# -------------------------
class Responsavel(Pessoa):
    PARENTESCO_CHOICES = [
        ("mae", "Mãe"),
        ("pai", "Pai"),
        ("avo", "Avô/Avó"),
        ("tio", "Tio/Tia"),
        ("outro", "Outro"),
    ]
    SEXO_CHOICES = [("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")]

    cpf = models.CharField(max_length=14, unique=True)
    parentesco = models.CharField(max_length=20, choices=PARENTESCO_CHOICES)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    cidade = models.CharField(max_length=100)


# -------------------------
# RF03 - Criança (herda de Pessoa)
# -------------------------
class Crianca(Pessoa):
    data_cadastro = models.DateField(auto_now_add=True)
    historico_situacao = models.TextField(blank=True, null=True)
    responsavel = models.ForeignKey(
        Responsavel, on_delete=models.CASCADE, related_name="criancas"
    )


# -------------------------
# RF03 extra - Profissional (herda de Pessoa)
# -------------------------
class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    ocupacao = models.CharField(max_length=100)  # campo de texto simples
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.ocupacao}"

# -------------------------
# RF01 - Usuário
# -------------------------
class Usuario(models.Model):
    PERFIL_CHOICES = [("profissional", "Profissional"), ("responsavel", "Responsável")]

    # Substituindo Pessoa abstrato por referência concreta
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, null=True, blank=True)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, null=True, blank=True)

    senha_hash = models.CharField(max_length=128)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)


# -------------------------
# RF02 - Acesso
# -------------------------
class Acesso(models.Model):
    usuario_perfil = models.CharField(max_length=20)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, null=True, blank=True)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, null=True, blank=True)


# -------------------------
# RF05 - Transtorno
# -------------------------
class Transtorno(models.Model):
    SEVERIDADE_CHOICES = [("leve", "Leve"), ("moderado", "Moderado"), ("grave", "Grave")]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    grau_severidade = models.CharField(max_length=10, choices=SEVERIDADE_CHOICES)

    def __str__(self):
        return self.nome


# -------------------------
# RF06 - Diagnóstico
# -------------------------
class Diagnostico(models.Model):
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    transtorno = models.ForeignKey(Transtorno, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    observacoes = models.TextField(blank=True, null=True)


# -------------------------
# RF07 - Sessão de Atendimento
# -------------------------
class Sessao(models.Model):
    STATUS_CHOICES = [
        ("agendada", "Agendada"),
        ("realizada", "Realizada"),
        ("cancelada", "Cancelada"),
    ]

    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    anotacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    duracao_minutos = models.PositiveIntegerField()


# -------------------------
# RF08 - Alerta
# -------------------------
class Alerta(models.Model):
    PRIORIDADE_CHOICES = [("baixa", "Baixa"), ("media", "Média"), ("alta", "Alta")]
    TIPO_CHOICES = [
        ("lembrete", "Lembrete"),
        ("emergencia", "Emergência"),
        ("atraso", "Atraso"),
    ]

    destinatario = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)


# -------------------------
# RF09 - Histórico de atendimento
# -------------------------
class Consulta(models.Model):
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    sessoes = models.ManyToManyField(Sessao, blank=True)
    diagnosticos = models.ManyToManyField(Diagnostico, blank=True)


# -------------------------
# RF10 - Visualização de alertas
# -------------------------
class Visualizacao(models.Model):
    alerta = models.ForeignKey(Alerta, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    visualizado = models.BooleanField(default=False)


# -------------------------
# RF11 - Relatório Clínico
# -------------------------
class RelatorioClinico(models.Model):
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_geracao = models.DateField(auto_now_add=True)
    resumo_diagnostico = models.TextField()
    resumo_sessoes = models.TextField()
    recomendacoes = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
