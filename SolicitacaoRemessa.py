from datetime import date, datetime
from enum import Enum

class StatusRemessa(Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em andamento"
    ENTREGUE = "Entregue"
    CANCELADA = "Cancelada"

class SolicitacaoRemessa:
    def __init__(self, data_solicitacao: date, data_entrega: date, status: StatusRemessa):
        self.data_solicitacao = data_solicitacao
        self.data_entrega = data_entrega
        self.status = status
    
    def get_solicitacao_remessa(self):
        return self
    
    def set_solicitacao_remessa(self, nova_solicitacao):
        if isinstance(nova_solicitacao, SolicitacaoRemessa):
            self.data_solicitacao = nova_solicitacao.data_solicitacao
            self.data_entrega = nova_solicitacao.data_entrega
            self.status = nova_solicitacao.status
            return True
        return False