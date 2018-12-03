from django.shortcuts import render, resolve_url as r, redirect
from django.contrib import messages
from Phoenix.devices.forms import EquipamentoForm, EmpresaForm, BlocoForm, SalaForm, MarcaForm, ModeloForm, ServicoForm, \
    SoftwareForm, SistemaOperacionalForm, VirtualizacaoForm, VirtualizacaoEquipamentoForm, ServicoEquipamentoForm, \
    SoftwareEquipamentoForm, SistemaOperacionalEquipamentoForm
from Phoenix.core.models import equipamento, software, software_equipamento, sistema_operacional_equipamento, \
    servico_equipamento, virtualizacao, virtualizacao_equipamento


# Create your views here.
def cadastro_empresa(request):
    form = EmpresaForm()
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('CadastroEmpresa'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Empresas'})


def cadastro_bloco(request):
    form = BlocoForm()
    if request.method == 'POST':
        form = BlocoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Blocos'})


def cadastro_sala(request):
    form = SalaForm()
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Salas'})


def cadastro_marca(request):
    form = MarcaForm()
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Marcas'})


def cadastro_modelo(request):
    form = ModeloForm()
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Modelos'})


def cadastro_equipamento(request):
    form = EquipamentoForm()
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('CadastroEquipamento'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Equipamentos'})


def gerenciar_equipamentos(request):
    dados = equipamento.objects.all()
    checkboxes = []
    if request.method == 'POST':
        for i in dados:
            try:
                checkboxes.append(request.POST[str(i.id)])
            except:
                pass
        if checkboxes:
            for item in checkboxes:
                dados.get(id=item).delete()
            messages.success(request, "Exclusão Realizada com Sucesso!")
        else:
            messages.error(request, "Selecione ao menos um equipamento para excluir")
        return redirect(r('GerenciarEquipamentos'))
    return render(request, 'gerenciar_equipamentos.html', {'dados': dados})


def detalhamento_equipamento(request, id_equipamento):
    if id_equipamento:
        dados = equipamento.objects.get(id=id_equipamento)
        softwares = software_equipamento.objects.select_related().filter(id_equipamento=id_equipamento)
        sos = sistema_operacional_equipamento.objects.select_related().filter(id_equipamento=id_equipamento)
        servicos = servico_equipamento.objects.select_related().filter(id_equipamento=id_equipamento)
        virtualizacoes = virtualizacao_equipamento.objects.select_related().filter(id_equipamento=id_equipamento)
    return render(request, 'detalhamento_equipamento.html', {'dados': dados, 'titulo': 'Detalhes do Equipamento', 'softwares': softwares, 'sos': sos, 'servicos': servicos, 'virtualizacoes': virtualizacoes})


def cadastro_servico(request):
    form = ServicoForm()
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Serviços'})


def cadastro_servico_equipamento(request):
    form = ServicoEquipamentoForm()
    if request.method == 'POST':
        form = ServicoEquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('CadastroServicoEquipamento'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Vincular Serviços a Equipamentos'})


def cadastro_software(request):
    form = SoftwareForm()
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Softwares'})


def cadastro_software_equipamento(request):
    form = SoftwareEquipamentoForm()
    if request.method == 'POST':
        form = SoftwareEquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('CadastroSoftwareEquipamento'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Vincular Softwares a Equipamentos'})


def cadastro_sistema_operacional(request):
    form = SistemaOperacionalForm()
    if request.method == 'POST':
        form = SistemaOperacionalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de SOs'})


def cadastro_sistema_operacional_equipamento(request):
    form = SistemaOperacionalEquipamentoForm()
    if request.method == 'POST':
        form = SistemaOperacionalEquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('CadastroSistemaOperacionalEquipamento'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Vincular SOs a Equipamentos'})


def cadastro_virtualizacao(request):
    form = VirtualizacaoForm()
    if request.method == 'POST':
        form = VirtualizacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('CadastroVirtualizacao'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Virtualização'})


def cadastro_virtualizacao_equipamento(request):
    form = VirtualizacaoEquipamentoForm()
    if request.method == 'POST':
        form = VirtualizacaoEquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('CadastroVirtualizacaoEquipamento'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Vincular Virtualizações a Equipamentos'})
