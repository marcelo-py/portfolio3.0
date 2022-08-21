from django.contrib import admin
from .models import Mensagem, Resposta


class MensagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'mensagem', 'mostrar', 'gostei')
    list_editable = ('mostrar', 'gostei')

    
class RespostasAdmin(admin.ModelAdmin):
    list_display = ('id', 'cometario')


admin.site.register(Mensagem, MensagemAdmin)
admin.site.register(Resposta, RespostasAdmin)