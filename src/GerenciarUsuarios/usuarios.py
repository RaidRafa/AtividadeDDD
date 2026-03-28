import secrets

class Usuario:
    def __init__(self, nome, email, senha, endereco):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._id = secrets.token_hex(1)
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def senha(self):
        return self._endereco

    @senha.setter
    def senha(self, nova_senha):
        if nova_senha == self._senha:
            print("A senha digitada é igual a antiga!")
        else:
            self._senha = nova_senha

    @property
    def id(self):
        return self._id

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco


