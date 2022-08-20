from django.shortcuts import render
from .models import MensagemForm


def index(request):
    if request.method != 'POST':
        return render(request, 'index.html', {
            'formulario': MensagemForm()
        })

    else:
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, 'index.html', {
            'formulario': MensagemForm()
        })
