from django import forms
import sys
from django.core.exceptions import ObjectDoesNotExist
from Phoenix.core.libs.conexaoAD3 import conexaoAD
from Phoenix.core.models import empresa, bloco, sala, equipamento, marca, modelo, servico, software, \
    sistema_operacional, virtualizacao, software_equipamento, virtualizacao_equipamento, \
    sistema_operacional_equipamento, servico_equipamento, servico_virtualizacao


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = empresa
        fields = ('nome_fantasia', 'razao_social', 'cnpj', 'logo', 'slogan', 'status')

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(EmpresaForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class BlocoForm(forms.ModelForm):
    class Meta:
        model = bloco
        fields = ('descricao', 'status',)

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(BlocoForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class SalaForm(forms.ModelForm):
    class Meta:
        model = sala
        fields = ('descricao', 'status')

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(SalaForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = equipamento
        fields = ('descricao','num_serie', 'ip', 'mac', 'imagem', 'monitorado', 'id_sala', 'id_marca', 'id_modelo', 'status')

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(EquipamentoForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class MarcaForm(forms.ModelForm):
    class Meta:
        model = marca
        fields = ('descricao', 'status')

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(MarcaForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class ModeloForm(forms.ModelForm):
    class Meta:
        model = modelo
        fields = ('descricao', 'status')

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(ModeloForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class ServicoForm(forms.ModelForm):
    class Meta:
        model = servico
        fields = ('nome', 'descricao', 'endereco', 'licenca', 'status')

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(ServicoForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = software
        fields = ('nome', 'descricao', 'licenca', 'arquitetura', 'status')

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(SoftwareForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class SistemaOperacionalForm(forms.ModelForm):
    class Meta:
        model = sistema_operacional
        fields = ('nome', 'descricao', 'licenca', 'arquitetura', 'status')

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(SistemaOperacionalForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class VirtualizacaoForm(forms.ModelForm):
    class Meta:
        model = virtualizacao
        fields = ('descricao', 'monitorado', 'ip', 'mac', 'id_sistema_operacional', 'status')

    def __init__(self, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(VirtualizacaoForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget = forms.TextInput(attrs={'class': 'item-checkbox', 'type': 'checkbox', 'checked': 'True'})


class SoftwareEquipamentoForm(forms.ModelForm):
    class Meta:
        model = software_equipamento
        fields = ('id_software', 'id_equipamento')


class VirtualizacaoEquipamentoForm(forms.ModelForm):
    class Meta:
        model = virtualizacao_equipamento
        fields = ('id_virtualizacao', 'id_equipamento')


class SistemaOperacionalEquipamentoForm(forms.ModelForm):
    class Meta:
        model = sistema_operacional_equipamento
        fields = ('id_sistema_operacional', 'id_equipamento')


class ServicoEquipamentoForm(forms.ModelForm):
    class Meta:
        model = servico_equipamento
        fields = ('id_servico', 'id_equipamento')


class ServicoVirtualizacaoForm(forms.ModelForm):
    class Meta:
        model = servico_virtualizacao
        fields = ('id_servico', 'id_virtualizacao')