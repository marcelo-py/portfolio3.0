from django.shortcuts import render
from .models import MensagemForm, Mensagem


def index(request):
    objetos = Mensagem.objects.all().filter(mostrar=True).order_by('-id')
    like_mensagens = Mensagem.objects.filter(gostei=True)

    if request.method != 'POST':
        return render(request, 'index.html', {
            'formulario': MensagemForm(),
            'mensagens': objetos,
            'mensagens_curtidas': like_mensagens,
        })

    else:
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, 'index.html', {
            'formulario': MensagemForm(),
            'mensagens': objetos,
            'mensagens_curtidas': like_mensagens,
        })

