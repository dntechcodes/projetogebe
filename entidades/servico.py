class Servico:
    def __init__(
        self,
        nome: str,
        descricao: str,
        preco: float,
        tempo_duracao: str
    ):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.tempo_duracao = tempo_duracao