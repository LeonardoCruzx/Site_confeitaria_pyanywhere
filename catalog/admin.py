from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.

# o decorador admin.register registra o modelo no django admin
# passado como parametro e a classe modelo admin que serve para colocar campos no campo de selecao e filtros
@admin.register(ModelDoces)
class ModelBolosAdmin(admin.ModelAdmin):
    #list display faz os campos aparecerem em cada objeto no django admin com seu conteudo
    list_display = ('nome','quantidade_de_fatias','categoria','preco')
    #list filter cria um filtro do lado direito com os itens
    list_filter = ('quantidade_de_fatias','categoria','preco')

@admin.register(ModelCategoria)
class ModelCategoriaDocesAdmin(admin.ModelAdmin):
    list_display = ('tipo',)


@admin.register(ModelQuantidadeFatias)
class ModelQuantidadeFatiasAdmin(admin.ModelAdmin):
    list_display = ('quantidade_de_fatias',)

