from datetime import date

# Se for utilizar enum para tipo do cliente
"""from enum import Enum
class TipoCliente(Enum):
    COMUM = 'Comum'
    VIP = 'Vip'"""

class Cliente():
    def __init__(self, nome_cliente: str, cpf: str, tipo: str, data_cadastro: date):
        self.__nome_cliente = nome_cliente
        self.__cpf = self.__validar_cpf(cpf)
        # Se for utilizar enum para tipo do cliente
        """self.__tipo = self.__validar_tipo(tipo)"""
        self.__tipo = tipo
        self.__data_cadastro = self.__validar_data(data_cadastro)
         
    def __validar_data(self, data):
        if isinstance(data, date):
            return data
        else:
            raise ValueError("Tipo de data inadequado.")
    
    # Se for utilizar enum para tipo do cliente
    """def __validar_tipo(self, tipo):
        tipo = tipo.lower()
        if isinstance(tipo, TipoCliente):
            return tipo
        else:
            raise ValueError("Tipo de cliente inexistente.")"""
    
    def __validar_cpf(self, cpf):
        aux = cpf.replace('-', '')
        aux = cpf.replace('.', '')

        # Verificando apenas a quantidade de dígitos
        if len(aux) == 11:
            return cpf
        else:
            raise ValueError("CPF invalido.")
        
    def get_nome_cliente(self):
        return self.__nome_cliente
    
    def set_nome_cliente(self, nome):
        self.__nome_cliente = nome
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = self.__validar_cpf(cpf)
    
    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, tipo):
        # Se for utilizar enum para tipo do cliente
        """self.__tipo = self.__validar_tipo(tipo)"""
        
        self.__tipo = tipo

    def get_data_cadastro(self):
        return self.__data_cadastro
    
    def set_data_cadastro(self, data):
        self.__data_cadastro = self.__validar_data(data)
