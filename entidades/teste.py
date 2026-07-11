from entidades.cliente import Cliente
from entidades.profissional import Profissional
from entidades.servico import Servico
from entidades.especialidade import Especialidade
from entidades.agendamento import Agendamento

# ---------- Cliente ----------
cliente1 = Cliente(
    nome='Gabriel',
    email='teste@teste.com',
    telefone='21999999999'
)
print('Cliente:', cliente1.getUlid(), cliente1.getNome(), cliente1.getEmail(), cliente1.getTelefone())

# ---------- Profissional ----------
profissional1 = Profissional(
    nome='Daniel',
    email='daniel@teste.com',
    telefone='21988888888',
    dias_trabalho=['segunda', 'quarta', 'sexta'],
    especialidade='Cabelo'
)
print('Profissional:', profissional1.getUlid(), profissional1.getNome(), profissional1.getEmail(),
      profissional1.getTelefone(), profissional1.getDiasTrabalho(), profissional1.getEspecialidade())

# ---------- Servico ----------
servico1 = Servico(
    nome='Corte de cabelo',
    descricao='Corte tradicional masculino',
    preco=50.0,
    tempo_duracao='30min'
)
print('Servico:', servico1.getUlid(), servico1.getNome(), servico1.getDescricao(),
      servico1.getPreco(), servico1.getTempoDuracao())

# ---------- Especialidade ----------
especialidade1 = Especialidade(nome='Cabelo')
print('Especialidade:', especialidade1.getUlid(), especialidade1.getNome())

# ---------- Agendamento ----------
agendamento1 = Agendamento(
    cliente=cliente1.getUlid(),
    profissional=profissional1.getUlid(),
    servico=servico1.getUlid(),
    status='confirmado',
    data='2026-07-15',
    horario_inicio='14:00',
    horario_fim='14:30'
)
print('Agendamento:', agendamento1.getUlid(), agendamento1.getCliente(), agendamento1.getProfissional(),
      agendamento1.getServico(), agendamento1.getStatus(), agendamento1.getData(),
      agendamento1.getHorarioInicio(), agendamento1.getHorarioFim())