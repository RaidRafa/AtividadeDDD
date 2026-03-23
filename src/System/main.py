
from src.Produtos.product_catalog import Produtos
import time

listProducts = list()

def separar():
    row = "-" * 50
    print(row)


pd1 = Produtos("Batom", "Passa na boca", 49.99)


pd2 = Produtos("Base", "Passa na cara", 149.90)

listProducts.append(pd1)
listProducts.append(pd2)

def catalogo():
    print("---------- Lista de produtos----------")
    for p in listProducts:
        print(f"""
            Produto: {p._name}
            Descrição: {p._descricao}
            Preço: {p._preco}
            Código: {p._token}""")

#   Inicio do sistema
separar()
print("                Bem vindo ao ERP!")
separar()
time.sleep(1)
print("""
              1) Gerenciar Usuários
              2) Gerenciar pedidos
              3) Catálogo
              4) Pagamentos""")
separar()

opcao = int(input("Escolha uma das opções(1-4): "))

if opcao < 1 or opcao > 4:
    print("Opção inválida!")

else:
    match opcao:
        case 1:
            print("Escolheu gerenciar Usuários")

        case 2:
            print("Escolheu gerenciar pedidos")

        case 3:
            catalogo()

        case 4:
            print("Escolheu pagamentos")



