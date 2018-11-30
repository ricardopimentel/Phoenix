from django.shortcuts import render, resolve_url as r, redirect
from django.contrib import messages
from Phoenix.devices.forms import EquipamentoForm, EmpresaForm, BlocoForm, SalaForm, MarcaForm, ModeloForm, ServicoForm, \
    SoftwareForm, SistemaOperacionalForm
from Phoenix.core.models import equipamento

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
    return render(request, 'detalhamento_equipamento.html', {'dados': dados, 'titulo': 'Detalhes do Equipamento'})


def cadastro_servico(request):
    form = ServicoForm()
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Serviços'})


def cadastro_software(request):
    form = SoftwareForm()
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Softwares'})


def cadastro_sistema_operacional(request):
    form = SistemaOperacionalForm()
    if request.method == 'POST':
        form = SistemaOperacionalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form, 'titulo': 'Cadastro de Sistemas Operacionais'})
