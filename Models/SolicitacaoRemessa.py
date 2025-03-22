from datetime import date, datetime
from enum import Enum

class StatusRemessa(Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em andamento"
    ENTREGUE = "Entregue"
    CANCELADA = "Cancelada"

class SolicitacaoRemessa:
    def __init__(self, data_solicitacao: date, data_entrega: date, status: StatusRemessa):
        self._data_solicitacao = data_solicitacao
        self._data_entrega = data_entrega
        self._status = status
    
    # Getters
    def get_data_solicitacao(self):
        return self._data_solicitacao
    
    def get_data_entrega(self):
        return self._data_entrega
    
    def get_status(self):
        return self._status
    
    # Setters
    def set_data_solicitacao(self, nova_data_solicitacao):
        if isinstance(nova_data_solicitacao, date):
            self._data_solicitacao = nova_data_solicitacao
            return True
        return False
    
    def set_data_entrega(self, nova_data_entrega):
        if isinstance(nova_data_entrega, date):
            self._data_entrega = nova_data_entrega
            return True
        return False
    
    def set_status(self, novo_status):
        if isinstance(novo_status, StatusRemessa):
            self._status = novo_status
            return True
        return False
    
