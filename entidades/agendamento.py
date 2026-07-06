class Agendamento:
    def __init__(
        self,
        cliente: str,
        profissional: str,
        servico: str,
        status: str,
        data: str,
        horario_inicio: str,
        horario_fim: str
    ):
        self.cliente = cliente
        self.profissional = profissional
        self.servico = servico
        self.status = status
        self.data = data
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        