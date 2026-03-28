from src.System.User_methods.User_Menu import menuUser
from src.Produtos.product_catalog import Produtos
import time

listProducts = list()

userList = list()

def separar():
    row = "-" * 50
    print(row)


pd1 = Produtos("Batom", "Passa na boca", 49.99, "LuizVitor")
pd2 = Produtos("Base", "Passa na cara", 149.90, "VitoriaSecredos")
pd3 = Produtos("Sombra", "Passa na cara", 180.90, "Abravanel")
pd4 = Produtos("Gloss", "Passa na cara", 25.90, "Channel")

listProducts.append(pd1)
listProducts.append(pd2)
listProducts.append(pd3)
listProducts.append(pd4)


def catalogo():
    print("---------- Lista de produtos ----------")
    for p in listProducts:
        print(f"""
            Produto: {p.name}
            Descrição: {p.descricao}
            Preço: {p.preco}
            Código: {p._token}""")

while True:
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
                menuUser()

            case 2:
                print("Escolheu gerenciar pedidos")

            case 3:
                catalogo()

            case 4:
                print("Escolheu pagamentos")



