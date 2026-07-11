from ulid import ULID


class Cliente:
    def __init__(
        self,
        nome: str,
        email: str,
        telefone: str,
        ulid: str = None,
    ):
        self.ulid = ulid if ulid else str(ULID())
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def getUlid(self):
        return self.ulid

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def getTelefone(self):
        return self.telefone