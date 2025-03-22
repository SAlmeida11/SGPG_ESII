from enum import Enum

class Status(Enum):
    ATIVA = "Ativa"
    INATIVA = "Inativa"

class Bomba():
    def __init__(self, litro: float, nome: str, status: Status):
        self.__litro = self.__validar_litro(litro)
        self.__nome = nome
        self.__status = self.__validar_status(status)
    
    def __validar_litro(self, litro):
        if isinstance(litro, float):
            return litro
        else:
            raise ValueError("Variavel litro deve ser float.")
    
    def __validar_status(self, status):
        if isinstance(status, Status):
            return status
        else:
            raise ValueError("Tipo de status invalido.")
    
    def get_litro(self):
        return self.__litro
    
    def set_litro(self, litro):
        self.__litro = self.__validar_litro(litro)
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = self.__validar_status(status)
