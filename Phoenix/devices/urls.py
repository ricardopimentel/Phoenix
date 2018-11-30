from django.conf.urls import url

from Phoenix.devices import views

urlpatterns = [
    url(r'^cadastro_empresa/$', views.cadastro_empresa, name='CadastroEmpresa'),
    url(r'^cadastro_bloco/$', views.cadastro_bloco, name='CadastroBloco'),
    url(r'^cadastro_sala/$', views.cadastro_sala, name='CadastroSala'),
    url(r'^cadastro_equipamento/$', views.cadastro_equipamento, name='CadastroEquipamento'),
    url(r'^cadastro_marca/$', views.cadastro_marca, name='CadastroMarca'),
    url(r'^cadastro_modelo/$', views.cadastro_modelo, name='CadastroModelo'),
    url(r'^cadastro_servico/$', views.cadastro_servico, name='CadastroServico'),
    url(r'^cadastro_software/$', views.cadastro_software, name='CadastroSoftware'),
    url(r'^cadastro_sistema_operacional/$', views.cadastro_sistema_operacional, name='CadastroSistemaOperacional'),
    url(r'^gerenciar_equipamentos/$', views.gerenciar_equipamentos, name='GerenciarEquipamentos'),
    url(r'^detalhamento_equipamento/(?P<id_equipamento>.+)$', views.detalhamento_equipamento, name='DetalhamentoEquipamento'),
]