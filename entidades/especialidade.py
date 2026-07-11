from ulid import ULID


class Especialidade:
    def __init__(self, nome, ulid: str = None):
        self.ulid = ulid if ulid else str(ULID())
        self.nome = nome

    def getUlid(self):
        return self.ulid

    def getNome(self):
        return self.nome