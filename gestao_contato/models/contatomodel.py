# -*- coding: utf-8 -*-
from django.db import models


class Contato(models.Model):
    """
    Classe de definição do contato
    """
    CANAL = (
        ('email', 'E-Mail'),
        ('celular', 'Celular'),
        ('fixo', 'Fixo'),
    )

    nome = models.CharField(
        max_length=128, help_text="Nome que descreva o contato")

    canal = models.CharField(choices=CANAL, max_length=10,
                             help_text="Tipo de canal de contato, podendo ser email, celular ou fixo")

    valor = models.CharField(
        max_length=254, help_text="Valor para o canal de contato")

    obs = models.CharField(
        max_length=254, help_text="Qualquer observação que seja pertinente", null=True, blank=True)
