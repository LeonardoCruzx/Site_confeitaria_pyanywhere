from django.shortcuts import render
from django.views.generic import ListView,UpdateView,CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.
class ModelBolosCreateView(CreateView):
    template_name = "criarbolos.html"
    form_class = InsereBoloForm
    success_url = reverse_lazy("listadedoces")


class ModelBolosListView(ListView):
    template_name = "listadedoces.html"
    model = ModelDoces
    context_object_name = "doces"

class ModelBolosUpdateView(UpdateView):
    template_name = "updatedebolos.html"
    model = ModelDoces
    fields = [
        'nome',
        'preco',
        'descricao'
    ]
    success_url = reverse_lazy("listadedoces")