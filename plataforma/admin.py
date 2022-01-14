from django.contrib import admin
from .models import Imovel, Imagem, DiasVisita, Visitas, Horario, Cidade

# Register your models here.
@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ("rua","valor","quartos","tamanho","cidade","tipo")   
    list_editable = ("valor","tipo")
    list_filter = ("cidade","tipo")

admin.site.register(DiasVisita)
admin.site.register(Imagem)
admin.site.register(Horario)
admin.site.register(Cidade)
admin.site.register(Visitas)