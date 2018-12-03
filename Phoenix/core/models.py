from __future__ import unicode_literals

from django.db import models

# Create your models here.
ARQUITETURA = (
        ('32', '32 bits'),
        ('64', '64 bits')
    )
SN = (
        ('s', 'Sim'),
        ('n', 'Não')
    )

class empresa(models.Model):
    nome_fantasia = models.CharField('Nome Fantasia', max_length=120)
    razao_social = models.CharField('Razão Social', max_length=150)
    cnpj = models.CharField('CNPJ', max_length=20)
    logo = models.ImageField('Imagem', upload_to='uploads/', default='uploads/default.png')
    slogan = models.CharField('Slogan', max_length=50)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.nome_fantasia)


class bloco(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.descricao)


class sala(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.descricao)


class marca(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.descricao)


class modelo(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.descricao)


class equipamento(models.Model):
    descricao = models.CharField('Descrição', max_length=200)
    num_serie = models.CharField('Número de Série', max_length=200)
    ip = models.CharField('Endereço IP', max_length=20)
    mac = models.CharField('Endereço MAC', max_length=20)
    monitorado = models.CharField('Necessita Monitoramento', max_length=50, choices=SN)
    id_sala = models.ForeignKey('Sala', sala)
    id_marca = models.ForeignKey('Marca', marca)
    id_modelo = models.ForeignKey('Modelo', modelo)
    imagem = models.ImageField('Imagem', upload_to='uploads/', default='uploads/default.png')
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.descricao+ '-'+ self.id_marca.descricao+ '-'+ self.num_serie)


class servico(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.CharField('Descrição', max_length=90)
    endereco = models.CharField('Endereço de Acesso', max_length=200, null=True)
    licenca = models.CharField('Chave de Licenciamento', max_length=50, null=True)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.nome)


class servico_equipamento(models.Model):
    id_equipamento = models.ForeignKey(equipamento)
    id_servico = models.ForeignKey(servico)


class software(models.Model):
    nome = models.CharField('Nome do Software', max_length=60)
    descricao = models.CharField('Descrição', max_length=90)
    licenca = models.CharField('Chave de Licenciamento', max_length=50, null=True)
    arquitetura = models.CharField('Arquitetura', max_length=60, choices=ARQUITETURA)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.nome)


class sistema_operacional(models.Model):
    nome = models.CharField('Nome do SO', max_length=60)
    descricao = models.CharField('Descrição', max_length=90)
    licenca = models.CharField('Chave de Licenciamento', max_length=50, null=True)
    arquitetura = models.CharField('Arquitetura', max_length=60, choices=ARQUITETURA)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.nome+ ' - '+ self.arquitetura)


class software_equipamento(models.Model):
    id_software = models.ForeignKey(software)
    id_equipamento = models.ForeignKey(equipamento)


class sistema_operacional_equipamento(models.Model):
    id_sistema_operacional = models.ForeignKey(sistema_operacional)
    id_equipamento = models.ForeignKey(equipamento)


class virtualizacao(models.Model):
    descricao = models.CharField('Descrição', max_length=90)
    monitorado = models.CharField('Necessita Monitoramento', max_length=50, choices=SN)
    ip = models.CharField('Endereço IP', max_length=20)
    mac = models.CharField('Endereço MAC', max_length=20)
    id_sistema_operacional = models.ForeignKey(sistema_operacional)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.descricao)


class virtualizacao_equipamento(models.Model):
    id_equipamento = models.ForeignKey(equipamento)
    id_virtualizacao = models.ForeignKey(virtualizacao)


class servico_virtualizacao(models.Model):
    id_servico = models.ForeignKey(servico)
    id_virtualizacao = models.ForeignKey(virtualizacao)


class config(models.Model):
    pasta_dig = models.CharField(max_length=200)
    dominio = models.CharField(max_length=200)
    endservidor = models.CharField(max_length=200)
    gadmin = models.CharField(max_length=200)
    ou = models.CharField(max_length=200)
    filter = models.TextField('Filtro')