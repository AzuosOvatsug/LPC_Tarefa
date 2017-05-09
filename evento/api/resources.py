from tastypie.resources import ModelResource
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization

class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class EventoResource(ModelResource):
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        excludes = ['password', 'is_active']


class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',),
            "cpf": ('exact',)
        }


class InscricaoResource(ModelResource):
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "tipoInscricao": ('exact', 'startswith',)
        }

class EventoCientificoResource(ModelResource):
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "issn": ('exact', 'startswith',)
        }

class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        

class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',),
            "cnpj": ('exact',)
        }

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }

class ArtigoCientificoResource(ModelResource):
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "titulo": ('exact', 'startswith',)
        }

class ArtigoAutorResource(ModelResource):
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "titulo": ('exact', 'startswith',)
        }
