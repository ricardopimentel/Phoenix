from __future__ import unicode_literals

from django.db import models

# Create your models here.
class empresa(models.Model):
    nome_fantasia = models.CharField('Nome Fantasia', max_length=120)
    razao_social = models.CharField('Razão Social', max_length=150)
    cnpj = models.CharField('CNPJ', max_length=20)
    logo = models.ImageField('Logotipo', upload_to='uploads/', default='uploads/default.png')
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
    TIPOS = (
        ('f', 'Fisíco'),
        ('s', 'Virtual')
    )

    SN = (
        ('s', 'Sim'),
        ('n', 'Não')
    )

    descricao = models.CharField('Descrição', max_length=200)
    num_serie = models.CharField('Número de Série', max_length=200)
    ip = models.CharField('Endereço IP', max_length=20)
    mac = models.CharField('Endereço MAC', max_length=20)
    licenca = models.CharField('Chave de Licenciamento', max_length=50, null=True)
    tipo = models.CharField('Tipo de Equipamento', max_length=50, choices=TIPOS)
    monitorado = models.CharField('Necessita Monitoramento', max_length=50, choices=SN)
    id_sala = models.ForeignKey('Sala', sala)
    id_marca = models.ForeignKey('Marca', marca)
    id_modelo = models.ForeignKey('Modelo', modelo)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.descricao)


class servico(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    endereco = models.CharField('Endereço de Acesso', max_length=200, null=True)
    licenca = models.CharField('Chave de Licenciamento', max_length=50, null=True)
    id_equipamento = models.ForeignKey(equipamento)
    status = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return str(self.descricao)


class config(models.Model):
    pasta_dig = models.CharField(max_length=200)
    dominio = models.CharField(max_length=200)
    endservidor = models.CharField(max_length=200)
    gadmin = models.CharField(max_length=200)
    ou = models.CharField(max_length=200)
    filter = models.TextField('Filtro')