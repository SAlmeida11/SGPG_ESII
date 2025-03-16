class ReservatorioCombustivel():
    def __init__(self, tipoCombustivel: str, capacidade: float, nivel: float, temperatura: float):
        self.__tipoCombustivel = tipoCombustivel
        self.__capacidade = capacidade
        self.__nivel = nivel
        self.__temperatura = temperatura

    def get_tipoCombustivel(self):
        return self.__tipoCombustivel
    
    def get_capacidade(self):
        return self.__capacidade
    
    def get_nivel(self):
        return self.__nivel
    
    def get_temperatura(self):
        return self.__temperatura
    
    def get_reservatorioCombustivel(self):
        return {
            'tipoCombustivel': self.get_tipoCombustivel(),
            'capacidade': self.get_capacidade(),
            'nivel': self.get_nivel(),
            'temperatura': self.get_temperatura()
        }
    
    def set_tipoCombustivel(self, tipoCombustivel):
        if isinstance(tipoCombustivel, str):
            self.__tipoCombustivel = tipoCombustivel
            return True
        return False
    
    def set_capacidade(self, capacidade):
        if isinstance(capacidade, float):
            self.__capacidade = capacidade
            return True
        return False
    
    def set_nivel(self, nivel):
        if isinstance(nivel, float):
            self.__nivel = nivel
            return True
        return False
    
    def set_temperatura(self, temperatura):
        if isinstance(temperatura, float):
            self.__temperatura = temperatura
            return True
        return False
