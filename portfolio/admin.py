from django.contrib import admin
from .models import Mensagem, Resposta, SobreMim


class MensagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'mensagem', 'mostrar', 'gostei')
    list_editable = ('mostrar', 'gostei')
    list_display_links = ('id', 'nome')


class RespostasAdmin(admin.ModelAdmin):
    list_display = ('id', 'cometario')


class SobreMimAdmin(admin.ModelAdmin):
    list_display = ('id', 'sobre', 'mostrar')
    list_display_links = ('id', 'sobre')
    list_editable = ('mostrar', )


admin.site.register(Mensagem, MensagemAdmin)
admin.site.register(Resposta, RespostasAdmin)
admin.site.register(SobreMim, SobreMimAdmin)
