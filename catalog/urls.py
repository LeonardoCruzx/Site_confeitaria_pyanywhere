    
from django.urls import path
from .models import *
from .views import *


urlpatterns = [
    path('criarbolos',ProdutosCreateView.as_view(),name='criarbolos'),
    path('lista_produtos',ProdutosListView.as_view(),name='lista_produtos'),
    path('updatedebolos/<pk>',ProdutosUpdateView.as_view(),name='updatedebolos'),
    path('filtrarProdutos/<pk>',filtrar_produto,name='filtrar_produtos'),
]