class Endereco:
    def __init__(self, rua, numero:int, bairro, cidade, uf):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self.uf = uf

    @property
    def rua(self):
        return self._rua

    @property
    def numero(self):
        return self._numero

    @property
    def bairro(self):
        return self._bairro

    @property
    def cidade(self):
        return self._cidade



