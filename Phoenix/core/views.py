from django.shortcuts import render, resolve_url as r, redirect
from django.contrib import messages
from Phoenix.core.forms import EquipamentoForm, EmpresaForm, BlocoForm, SalaForm, MarcaForm, ModeloForm, ServicoForm
from Phoenix.core.models import empresa

# Create your views here.
def home(request):
    parametros = {'menu': (
        {'titulo': 'Cadastro de Empresa', 'url': r('CadastroEmpresa')},
        {'titulo': 'Cadastro de Bloco', 'url': r('CadastroBloco')},
        {'titulo': 'Cadastro de Sala', 'url': r('CadastroSala')},
        {'titulo': 'Cadastro de Marca', 'url': r('CadastroMarca')},
        {'titulo': 'Cadastro de Modelo', 'url': r('CadastroModelo')},
        {'titulo': 'Cadastro de Equipamento', 'url': r('CadastroEquipamento')},
        {'titulo': 'Cadastro de Serviço', 'url': r('CadastroServico')},
    )}
    return render(request, 'index.html', parametros)


def cadastro_empresa(request):
    form = EmpresaForm()
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect(r('CadastroEmpresa'))
    return render(request, 'cadastro_geral.html', {'form': form})


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
        form = EquipamentoForm(request.POST)
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