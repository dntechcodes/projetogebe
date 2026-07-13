from ulid import ULID


class Servico:
    def __init__(
        self,
        nome: str,
        descricao: str,
        preco: float,
        tempo_duracao: str,
        ulid: str = None
    ):
        self.ulid = ulid if ulid else str(ULID())
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.tempo_duracao = tempo_duracao

    def setUlid(self, ulid):
        self.ulid = ulid
        return self

    def setNome(self, nome):
        self.nome = nome
        return self

    def setDescricao(self, descricao):
        self.descricao = descricao
        return self

    def setPreco(self, preco):
        self.preco = preco
        return self

    def setTempoDuracao(self, tempo_duracao):
        self.tempo_duracao = tempo_duracao
        return self

    def getUlid(self):
        return self.ulid

    def getNome(self):
        return self.nome

    def getDescricao(self):
        return self.descricao

    def getPreco(self):
        return self.preco

    def getTempoDuracao(self):
        return self.tempo_duracao