from django import forms
import sys
from django.core.exceptions import ObjectDoesNotExist
from Phoenix.core.libs.conexaoAD3 import conexaoAD
from Phoenix.core.models import empresa, bloco, sala, equipamento, marca, modelo, servico


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = empresa
        fields = ('nome_fantasia', 'razao_social', 'cnpj', 'logo', 'slogan', 'status')


class BlocoForm(forms.ModelForm):
    class Meta:
        model = bloco
        fields = ('descricao', 'status',)


class SalaForm(forms.ModelForm):
    class Meta:
        model = sala
        fields = ('descricao', 'status')


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = equipamento
        fields = ('descricao','num_serie', 'ip', 'mac', 'licenca', 'imagem', 'tipo', 'monitorado', 'id_sala', 'id_marca', 'id_modelo', 'status')


class MarcaForm(forms.ModelForm):
    class Meta:
        model = marca
        fields = ('descricao', 'status')


class ModeloForm(forms.ModelForm):
    class Meta:
        model = modelo
        fields = ('descricao', 'status')


class ServicoForm(forms.ModelForm):
    class Meta:
        model = servico
        fields = ('descricao', 'endereco', 'licenca', 'id_equipamento', 'status')