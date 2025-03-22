from datetime import date
from decimal import Decimal

class Vinculo():
    def __init__(self, dataContratacao, salario, status):
        self.setDataContratacao(dataContratacao)
        self.setSalario(salario)
        self.setStatus(status)

    def getDataContratacao(self):
        return self.__dataContratacao
    def getSalario(self):
        return self.__salario
    def getStatus(self):
        return self.__status
    
    def setDataContratacao(self, dataContratacao):
        if isinstance(dataContratacao, date):
            self.__dataContratacao = dataContratacao
        else:
            raise ValueError("Data incorreta.")
    def setSalario(self, novoSalario):
        if isinstance(novoSalario, float) and novoSalario > 0:
            self.__salario = novoSalario
        else:
            raise ValueError("Salario incorreto ou menor/igual a 0.")
    def setStatus(self, novoStatus):
        if isinstance(novoStatus, bool):
            self.__status = novoStatus
        else:
            raise ValueError("Status incorreto.")