class Servico():
    def __init__(self, descricao: str, valor: float, duracaoEstimada: float, disponivel: bool):
        self.__descricao = descricao
        self.__valor = valor
        self.__duracaoEstimada = duracaoEstimada
        self.__disponivel = disponivel

    def get_descricao(self):
        return self.__descricao
    
    def get_valor(self):
        return self.__valor
    
    def get_duracaoEstimada(self):
        return self.__duracaoEstimada
    
    def get_disponivel(self):
        return self.__disponivel
    
    def get_servico(self):
        return {
            'descricao': self.get_descricao(),
            'valor': self.get_valor(),
            'duracaoEstimada': self.get_duracaoEstimada(),
            'disponivel': self.get_disponivel()
        }
    
    def set_descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao
            return True
        return False
    
    def set_valor(self, valor):
        if isinstance(valor, float):
            self.__valor = valor
            return True
        return False
    
    def set_duracaoEstimada(self, duracaoEstimada):
        if isinstance(duracaoEstimada, float):
            self.__duracaoEstimada = duracaoEstimada
            return True
        return False
    
    def set_disponivel(self, disponivel):
        if isinstance(disponivel, bool):
            self.__disponivel = disponivel
            return True
        return False