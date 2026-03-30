from src.GerenciarUsuarios.User_methods.User_Menu import menuUser
from src.Produtos.Product_methods.product_methods import catalogo
import time

userList = list()

def separar():
    row = "-" * 50
    print(row)


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



