from ulid import ULID


class Profissional:
    def __init__(
        self,
        nome: str,
        email: str,
        telefone: str,
        dias_trabalho: list,
        especialidade: str,
        ulid: str = None
    ):
        self.ulid = ulid if ulid else str(ULID())
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.dias_trabalho = dias_trabalho
        self.especialidade = especialidade


    def setUlid(self, ulid):
        self.ulid = ulid
        return self

    def setNome(self, nome):
        self.nome = nome
        return self

    def setEmail(self, email):
        self.email = email
        return self

    def setTelefone(self, telefone):
        self.telefone = telefone
        return self

    def setDiasTrabalho(self, dias_trabalho):
        self.dias_trabalho = dias_trabalho
        return self

    def setEspecialidade(self, especialidade):
        self.especialidade = especialidade
        return self

    def getUlid(self):
        return self.ulid

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def getTelefone(self):
        return self.telefone

    def getDiasTrabalho(self):
        return self.dias_trabalho

    def getEspecialidade(self):
        return self.especialidade