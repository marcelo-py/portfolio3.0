from django.contrib import admin
from .models import Mensagem


class MensagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'mensagem', 'mostrar')
    list_editable = ('mostrar',)


admin.site.register(Mensagem, MensagemAdmin)
