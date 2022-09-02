from django.db import models
from django.utils import timezone
from django.forms import ModelForm


class Mensagem(models.Model):
    nome = models.CharField(max_length=20, blank=False, default='Anônimo')
    mensagem = models.TextField(max_length=200, blank=False)
    mostrar = models.BooleanField(default=True)
    data = models.DateTimeField(default=timezone.now)
    gostei = models.BooleanField(default=False)

    def __str__(self):
        return self.mensagem


class Resposta(models.Model):
    nome = models.CharField(max_length=15, default='Marcelo', blank=False)
    resposta = models.TextField(blank=False)
    cometario = models.ForeignKey(Mensagem, on_delete=models.CASCADE, related_name='respostas')

    def __str__(self):
        return self.resposta


class SobreMim:
    sobre = models.TextField()
    mostrar = models.BooleanField(default=False)


class MensagemForm(ModelForm):
    class Meta:
        model = Mensagem
        exclude = ('mostrar', 'data', 'gostei')

