from django.shortcuts import render, resolve_url as r, redirect


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