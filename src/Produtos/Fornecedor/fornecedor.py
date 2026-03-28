import re


class Fornecedor:
    def __init__(self, nome_f, cnpj_f, ramo_f):
        self.nome = nome_f
        if self.validarCnpj(cnpj_f):
            self._cnpj = cnpj_f
        else:
            raise ValueError("CNPJ inválido!")
        self.ramo = ramo_f

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome

    @property
    def cnpj(self):
        return self.cnpj

    @property
    def ramo(self):
        return self.ramo

    def validarCnpj(self, cnpj):
        padrao = r'^\d{5}-?\d{3}$'
        if re.match(padrao, cnpj):
            return True
        return False

