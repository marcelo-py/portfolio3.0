from django.shortcuts import render
from .models import MensagemForm, Mensagem, SobreMim
from requests import post
from json import loads
from decouple import config

def index(request):
    objetos = Mensagem.objects.all().filter(mostrar=True).order_by('-id')
    sobre_mim = SobreMim.objects.all()[0]

    like_mensagens = Mensagem.objects.filter(gostei=True)

    if request.method != 'POST':
        
        return render(request, 'index.html', {
            'formulario': MensagemForm(),
            'mensagens': objetos,
            'mensagens_curtidas': like_mensagens,
            'sobremim': sobre_mim,
        })

    else:
        captcha_token = request.POST.get('g-recaptcha-response')
        cap_url = 'https://www.google.com/recaptcha/api/siteverify'
        cap_secret = config('cap_secret') #variavel desacoplada para segurança

        cap_data = {'secret': cap_secret, 'response': captcha_token}
        cap_server_response = post(url=cap_url, data=cap_data)
        cap_json = loads(cap_server_response.text)

        if not cap_json['success']:
            return render(request, 'index.html', {
            'formulario': MensagemForm(),
            'mensagens': objetos,
            'mensagens_curtidas': like_mensagens,
            'sobremim': sobre_mim,
        })


        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, 'index.html', {
            'formulario': MensagemForm(),
            'mensagens': objetos,
            'mensagens_curtidas': like_mensagens,
            'sobremim': sobre_mim,
        })

