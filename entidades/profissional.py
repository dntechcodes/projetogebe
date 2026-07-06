class Profissional:
    def __init__(
        self,
        nome: str,
        email: str,
        telefone: str,
        dias_trabalho: list,
        especialidade: str
    ):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.dias_trabalho = dias_trabalho
        self.especialidade = especialidade