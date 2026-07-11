from ulid import ULID

class Agendamento:
    def __init__(
        self,
        cliente: str,
        profissional: str,
        servico: str,
        status: str,
        data: str,
        horario_inicio: str,
        horario_fim: str,
        ulid: str = None
    ):
        self.ulid = ulid if ulid else str(ULID())
        self.cliente = cliente
        self.profissional = profissional
        self.servico = servico
        self.status = status
        self.data = data
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim

    def getUlid(self):
        return self.ulid

    def getCliente(self):
        return self.cliente

    def getProfissional(self):
        return self.profissional

    def getServico(self):
        return self.servico

    def getStatus(self):
        return self.status
    def getData(self):
        return self.data

    def getHorarioInicio(self):
        return self.horario_inicio

    def getHorarioFim(self):
        return self.horario_fim        