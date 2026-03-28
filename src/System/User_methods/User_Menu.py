from src.GerenciarUsuarios.usuarios import Usuario

userList = list()

user1 = Usuario("Rogério", "rogerioung@gmail.com", "4s6g54s65g4", "Rua italo adami")
user2 = Usuario("Rogério", "rogerioung@gmail.com", "4s6g54s65g4", "Rua italo adami")
user3 = Usuario("Rogério", "rogerioung@gmail.com", "4s6g54s65g4", "Rua italo adami")
user4 = Usuario("Rogério", "rogerioung@gmail.com", "4s6g54s65g4", "Rua italo adami")

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
            Endereço: {u.endereco}""")

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