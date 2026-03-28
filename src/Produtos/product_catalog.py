import secrets
from src.Produtos.Fornecedor.fornecedor import Fornecedor

class Produtos:
    def __init__(self, p_name, p_descript, p_price, p_fornecedor:Fornecedor.nome):
        self._name = p_name
        self._descricao = p_descript
        self._preco = p_price
        self._fornecedor = p_fornecedor
        self._token = secrets.token_hex(2)

    @property
    def name(self):
        return self._name

    @name.setter
    def edit_name(self, novo_nome):
        if not novo_nome.strip():   # strip lê se a variável está vazia
             print("Precisa de um nome!")

        else:
            self._name = novo_nome

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if not nova_descricao.strip():  # strip lê se a variável está vazia
            print("Descrição não pode ser vazia")

        else:
            self._descricao = nova_descricao

    @property
    def fornecedor(self):
        return self._fornecedor

    @fornecedor.setter
    def fornecedor(self, novo_fornecedor):
        self._fornecedor = novo_fornecedor

    @property
    def preco(self):
        return self._preco

    @descricao.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
             print("Não pode ter um preço negativo.")

        else:
            self._preco = novo_preco




