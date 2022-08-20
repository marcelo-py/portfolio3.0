from django.shortcuts import render
from .models import MensagemForm, Mensagem


def index(request):
    objetos = Mensagem.objects.all().filter(mostrar=True)
    if request.method != 'POST':
        return render(request, 'index.html', {
            'formulario': MensagemForm(),
            'mensagens': objetos,
        })

    else:
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, 'index.html', {
            'formulario': MensagemForm(),
            'mensagens': objetos,
        })
