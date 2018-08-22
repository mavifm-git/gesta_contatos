# -*- coding: utf-8 -*-
from tastypie.resources import ModelResource
from tastypie import fields
from ..models import Contato
from tastypie.authorization import Authorization
from .. import __version__


class ContatoResource(ModelResource):
    """
    Resource Contato
    model: Contato
    metodos: get, put, post e delete
    autorizacao: Nenhuma (aberto)
    """
    class Meta:
        resource_name = 'contato'
        queryset = Contato.objects.all()
        allowed_methods = ['get', 'put', 'post', 'delete']
        authorization = Authorization()

    def build_schema(self):
        """
        Metodo que escreve o schema, sobreescrevendo da classe base
        """
        base_schema = {}  # super(ContatoResource, self).build_schema()

        #del base_schema['fields']
        #del base_schema['allowed_detail_http_methods']
        #del base_schema['allowed_list_http_methods']

        base_schema.update({
            'methods': ["get", "put", "post", "delete"],
            'title': 'Contato',
            'description': 'API para um serviço de gestão de contatos',
            'contact': {
                'name': 'Developer Team',
                'url': 'http://devtest.com',
                'email': 'dev.team@devtest.com',
            },
            'license': {
                'name': 'MIT License',
                'url': 'https://opensource.org/licenses/MIT',
            },
            'version': __version__
        })

        base_schema.update({
            'schemas': {
                'Contato': {
                    'title': 'Root Type for Contato',
                    'description': 'The root of the Contato type''s schema.',
                    'required': ['nome', 'canal', 'valor'],
                    'type': 'object',
                    'properties': {
                        'id': {
                            'description': 'Identificador único',
                            'type': 'string'
                        },
                        'nome': {
                            'description': 'Nome que descreva o contato',
                            'type': 'string'
                        },
                        'canal': {
                            'description': 'Tipo de canal de contato, podendo ser email, celular ou fixo',
                            'type': 'string'
                        },
                        'valor': {
                            'description': 'Valor para o canal de contato',
                            'type': 'string'
                        },
                        'obs': {
                            'description': 'Qualquer observação que seja pertinente',
                            'type': 'string'
                        }
                    }
                }
            }
        })

        return base_schema
