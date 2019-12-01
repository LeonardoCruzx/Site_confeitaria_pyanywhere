from django import forms
from .models import *

class InsereBoloForm(forms.ModelForm):
    class Meta:
        model = ModelDoces

        fields = [
            'nome',
            'descricao'
        ]