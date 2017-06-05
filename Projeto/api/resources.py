from tastypie.resources import ModelResource
from tastypie import fields, utils
from Projeto.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized

class UsuarioResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized ('Não pode excluir a Lista!')

    class Meta:
        queryset = Usuario.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        excludes = ['password', 'is_active']
        filtering = {
            "nome": ('exact', 'startswith',)
        }

class ProjetoResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized ('Não pode excluir a Lista!')

    class Meta:
        queryset = Projeto.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }


class TarefaResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized ('Não pode excluir a Lista!')

    def obj_create(self, bundle, **kwargs):
        p = bundle.data['projeto'].split("/")

        tipo = Tarefa()
        tipo.nome = bundle.data['nome'].upper()

        if not (Tarefa.objects.filter(projeto=p[4], nome=tipo)):

            tipo.nome = bundle.data["nome"]
            tipo.dataEHoraDeInicio = bundle.data["dataEHoraDeInicio"]
            tipo.usuario = Usuario.objects.get(pk=int(p[4]))
            tipo.projeto = Projeto.objects.get(pk=int(p[4]))

            tipo.save()
            bundle.obj = tipo
            return bundle

        else:
            raise Unauthorized('Tarefa já está cadastrada a um projeto!')

    class Meta:
        queryset = Tarefa.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }


class ProjetoUsuarioResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized ('Não pode excluir a Lista!')

    class Meta:
        queryset = ProjetoUsuario.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "usuario": ('exact', 'startswith',),
            "projeto": ('exact', 'startswith',)
        }
