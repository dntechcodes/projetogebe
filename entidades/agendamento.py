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

    def setUlid(self, ulid):
        self.ulid = ulid
        return self

    def setCliente(self, cliente):
        self.cliente = cliente
        return self

    def setProfissional(self, profissional):
        self.profissional = profissional
        return self

    def setServico(self, servico):
        self.servico = servico
        return self

    def setStatus(self, status):
        self.status = status
        return self

    def setData(self, data):
        self.data = data
        return self

    def setHorarioInicio(self, horario_inicio):
        self.horario_inicio = horario_inicio
        return self

    def setHorarioFim(self, horario_fim):
        self.horario_fim = horario_fim
        return self

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