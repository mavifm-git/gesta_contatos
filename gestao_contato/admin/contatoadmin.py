# -*- coding: utf-8 -*-
from django.contrib import admin
from ..models import Contato


class AccountUserAdmin(admin.ModelAdmin):
    """
    Classe admin do model contato para facilitar visualização das informções manipuladas, visto que o projeto não possui front
    possui opção de procura por nome
    """

    ordering = ("nome",)
    list_display = ("nome", "canal", "valor", "obs",)

    search_fields = ["nome"]

admin.site.register(Contato, AccountUserAdmin)
