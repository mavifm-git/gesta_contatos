# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from models import Contato
import json


class TestCase(TestCase):
    """
    Realiza o teste utilizando request a API e avaliando seu retorno
    """

    def setUp(self):
        self.c = Client()

    def test_contato_api(self):
        """
        teste da api:
        1- Insere um contato e verifica o status_code retornado
        2- Insere outro contato e verifica se não veio status_code diferente
        3- Faz um GET e verifica se o retorno da API corresponde com o numero de contatos inseridos (2)
        4- guarda a ID do primeiro contato inserido
        5- faz um PUT para atualizar o valor de 'nome' do contato
        6- Verifica se o nome foi realmente alterado 
        7- Deleta esse id do contato
        8- Verifica se a contagem de contatos esta correta (1)
        """
        response = self.c.post("/api/v1/contato/", json.dumps({"nome": "Rodrigo Teste 1",
                                                               "canal": "email", "valor": "rodrigobiassusi@gmail.com"}), content_type="application/json")

        self.assertEqual(response.status_code, 201)

        response = self.c.post(
            "/api/v1/contato/", json.dumps({"nome": "Rodrigo Teste 2", "canal": "celular", "valor": "21995241837"}), content_type="application/json")
        self.assertNotEqual(response.status_code, 400)

        response = self.c.get("/api/v1/contato/")
        objects = response.json()["objects"]
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0]["nome"], "Rodrigo Teste 1")
        self.assertEqual(objects[1]["nome"], "Rodrigo Teste 2")

        id_1 = objects[0]["id"]
        response = self.c.put("/api/v1/contato/1/",
                              json.dumps({"nome": "Rodrigo Teste 3"}), content_type="application/json")
        self.assertEqual(response.status_code, 204)

        response = self.c.get("/api/v1/contato/")
        objects = response.json()["objects"]
        self.assertNotEqual(objects[0]["nome"], "Rodrigo Teste 1")
        self.assertEqual(objects[0]["nome"], "Rodrigo Teste 3")

        self.c.delete("/api/v1/contato/1/")

        response = self.c.get("/api/v1/contato/")
        objects = response.json()["objects"]
        self.assertNotEqual(len(objects), 2)
        self.assertEqual(len(objects), 1)
