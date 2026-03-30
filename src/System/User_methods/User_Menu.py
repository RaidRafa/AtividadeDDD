from src.GerenciarUsuarios.Endereco.endereco import Endereco
from src.GerenciarUsuarios.usuarios import Usuario
import time

userList = list()

user1 = Usuario("Rogério", "rogerioung@gmail.com", "4s6g54s65g4", Endereco("Rua maresias", "170", "Jardim Maragojipe", "Itaquaquecetuba", "SP"))
user2 = Usuario("Rogério", "rogerioung@gmail.com", "4s6g54s65g4", Endereco("Rua maresias", "170", "Jardim Maragojipe", "Itaquaquecetuba", "SP"))
user3 = Usuario("Rogério", "rogerioung@gmail.com", "4s6g54s65g4", Endereco("Rua maresias", "170", "Jardim Maragojipe", "Itaquaquecetuba", "SP"))
user4 = Usuario("Rogério", "rogerioung@gmail.com", "4s6g54s65g4", Endereco("Rua maresias", "170", "Jardim Maragojipe", "Itaquaquecetuba", "SP"))

userList.append(user1)
userList.append(user2)
userList.append(user3)
userList.append(user4)

def userManager():
    print("---------- Usuários ----------")
    for u in userList:
        print(f"""
            ID: {u.id}
            Usuário: {u.nome}
            E-mail: {u.email}
            Endereço: {u.endereco.rua, u.endereco.numero, u.endereco.bairro, u.endereco.cidade, u.endereco.uf}""")
    time.sleep(1)

def editUser():

    try:
        procurar = input("Digite o Id do Usuário que deseja editar: ")
    except ValueError:
        print("Digite apenas numeros!")
        time.sleep(1.5)
        return

    usuario_encontrado = None

    for u in userList:
        if procurar == u.id:
            usuario_encontrado = u
            break


    if usuario_encontrado:
        print(f""" Informações 
                Nome: {u.nome}
                Email: {u.email}
                Senha: {u.senha}
                Endereço: {u.endereco.rua, u.endereco.numero, u.endereco.bairro, u.endereco.cidade, u.endereco.uf}""")
        time.sleep(1)


        print(f""" O que deseja editar? 
                        1) Nome
                        2) Email
                        3) Endereço
                        4) Senha""")
        time.sleep(1)
        opcao = int(input("Opção: "))

        match opcao:
            case(1):
                novo_nome = str(input("Digite o novo nome: "))
                usuario_encontrado.nome = novo_nome

                print(f"O Usuário com o ID {u.id} trocou o nome para {novo_nome}")

            case(2):
                novo_email = str(input("Digite o novo email: "))
                usuario_encontrado.email = novo_email

                print(f"O Usuário com o ID {u.id} trocou o email para {novo_email}")

            case(3):
                pass


            case(4):
                nova_senha = str(input("Digite a nova senha: "))
                usuario_encontrado.senha = nova_senha

                print(f"O Usuário com o ID {u.id} trocou a senha para {nova_senha}")

    else:
        print("Usuário não encontrado!")




def menuUser():
    print("---------- Gerenciar Usuários ----------")
    print(f"""
                1) Listar Usuários
                2) Editar Usuário
                3) Deletar Usuário""")
    opcao = int(input("Escolha uma das opções(1-3): "))

    match opcao:
        case(1):
            userManager()
        case(2):
            editUser()