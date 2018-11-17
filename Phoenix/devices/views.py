from django.shortcuts import render, resolve_url as r, redirect
from django.contrib import messages
from Phoenix.devices.forms import EquipamentoForm, EmpresaForm, BlocoForm, SalaForm, MarcaForm, ModeloForm, ServicoForm
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
    return render(request, 'cadastro_geral.html', {'form': form})


def gerenciar_equipamentos(request):
    dados = equipamento.objects.all()
    return render(request, 'gerenciar_equipamentos.html',{'dados': dados})


def cadastro_bloco(request):
    form = BlocoForm()
    if request.method == 'POST':
        form = BlocoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form})


def cadastro_sala(request):
    form = SalaForm()
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form})


def cadastro_marca(request):
    form = MarcaForm()
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form})


def cadastro_modelo(request):
    form = ModeloForm()
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form})


def cadastro_equipamento(request):
    form = EquipamentoForm()
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form})


def cadastro_servico(request):
    form = ServicoForm()
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('Home'))
    return render(request, 'cadastro_geral.html', {'form': form})