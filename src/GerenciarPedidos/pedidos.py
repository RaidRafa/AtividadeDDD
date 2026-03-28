import secrets
from src.GerenciarUsuarios.usuarios import Usuario
from src.Produtos.product_catalog import Produtos

class Pedido:
    def __init__(self):
        self._id = secrets.token_hex(4).upper()
        self.client = Usuario.nome
        self.end_entrega = Usuario.endereco
        self.itens = []
        self._status = "Aberto"

    @property
    def id(self):
        return self._id

    def adicionar_produto(self):
        self.itens.append(Produtos)
        print(f"{Produtos.name} adicionado ao pedido {self.id}")

    @property
    def total(self):
        return sum(itens.preco for itens in self.itens)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        match novo_status:
            case "Pago" | "Enviado" | "Cancelado":
                self._status = novo_status
            case _:
                print("Status inválido!")

    def exibir_resumo(self):
        print(f"\n--- RESUMO DO PEDIDO: {self._id} ---")
        print(f"Cliente: {self.client}")
        for item in self.itens:
            print(f"- {item.name}: R$ {item.preco:.2f}")
        print(f"TOTAL: R$ {self.total:.2f}")
        print(f"Status: {self._status}\n")
