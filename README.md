gestao_contato
==============

API para um serviço de gestão de contatos.

Requisitos
==========

Core
----
* Python 2.7
* Django 1.11
* Tastypie

Opcional
--------
* pip
* virtual_env 

Instalação
==========
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py createsuperuser

Teste
=====
* python manage.py test

Utilização
==========
Rodar o servidor django:
* python manage.py runserver

1. Acesso a interface admin:
* http://localhost:8000/admin
preencha usuario e senha criados no comando "python manage.py createsuperuser"


------

2. Acesso via API

* Endereço da API:
  /api/v1
  
* Endereço do Schema:
  /api/v1/contato/schema/
  
* Endpoint contato:
  /api/v1/contato/


