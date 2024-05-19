import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Garante


import pytest
from pytest_bdd import scenarios, given, when, then
from carrinho_compras import CarrinhoCompras
scenarios('features/carrinho_compras.feature')


@pytest.fixture
def carrinho():
   return CarrinhoCompras()


@given('que tenho um carrinho de compras com item "Camiseta" e preço R$ 29.99')
def adicionar_item_inicial(carrinho):
   carrinho.adicionar_item("Camiseta", 29.99)


@when('eu adiciono o item "Calça" com o preço R$ 49.99')
def adicionar_item_calca(carrinho):
   carrinho.adicionar_item("Calça", 49.99)


@then('o total do carrinho de compras deve ser R$ 79.98')
def verificar_total(carrinho):
   assert carrinho.total() == 79.98
   
   

@when('eu removo o item do carrinho')
def remover_item(carrinho):
   carrinho.remover_item()


@then('o carrinho de compras deve estar vazio')
def verificar_carrinho_vazio(carrinho):
   assert carrinho.esta_vazio()
