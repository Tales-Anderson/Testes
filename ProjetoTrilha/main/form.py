from django.forms import ModelForm
from .models import *


class ApartamentoForm(ModelForm):
    class Meta:
        model = Apartamento
        fields = ['valor', 'andar', 'tamM3', 'numero', 'residente', 'qtdQuartos', 'qtdBanheiros', 'descricao', 'disponivel']