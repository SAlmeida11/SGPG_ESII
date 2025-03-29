from datetime import datetime
from typing import List
from enum import Enum

class StatusOrdemServico(Enum):
    PENDENTE = "Pendente"
    CONCLUIDA = "Concluída"
    CANCELADA = "Cancelada"

class OrdemServico:
    def __init__(self, data_solicitacao: datetime, data_conclusao: datetime = None, descricao: str = "", horario_marcado: str = "", observacoes: str = "", status: StatusOrdemServico = StatusOrdemServico.PENDENTE, itens_adicionais: List[str] = None):
        self._data_solicitacao = data_solicitacao
        self._data_conclusao = data_conclusao
        self._descricao = descricao
        self._horario_marcado = horario_marcado
        self._observacoes = observacoes
        self._status = status
        self._itens_adicionais = itens_adicionais if itens_adicionais else []


    def get_data_solicitacao(self):
        return self._data_solicitacao

    def set_data_solicitacao(self, data_solicitacao: datetime):
        self._data_solicitacao = data_solicitacao

    def get_data_conclusao(self):
        return self._data_conclusao

    def set_data_conclusao(self, data_conclusao: datetime):
        self._data_conclusao = data_conclusao

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao: str):
        self._descricao = descricao

    def get_horario_marcado(self):
        return self._horario_marcado

    def set_horario_marcado(self, horario_marcado: str):
        self._horario_marcado = horario_marcado

    def get_observacoes(self):
        return self._observacoes

    def set_observacoes(self, observacoes: str):
        self._observacoes = observacoes

    def get_status(self):
        return self._status

    def set_status(self, status: StatusOrdemServico):
        self._status = status

    def get_itens_adicionais(self):
        return self._itens_adicionais

    def set_itens_adicionais(self, itens_adicionais: List[str]):
        self._itens_adicionais = itens_adicionais

    def registrar_ordem_de_servico(self):
        print(f"Ordem de serviço registrada: {self._descricao} com status {self._status.value}")
