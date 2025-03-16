from datetime import date, time

class PontoTrabalho():
    def __init__(self, dataRegistro: date, horaChegada: time, horaSaida: time, horasTrabalhadas: float):
        self.__dataRegistro = dataRegistro
        self.__horaChegada = horaChegada
        self.__horaSaida = horaSaida
        self.__horasTrabalhadas = horasTrabalhadas

    def get_dataRegistro(self):
        return self.__dataRegistro
    
    def get_horaChegada(self):
        return self.__horaChegada
    
    def get_horaSaida(self):
        return self.__horaSaida
    
    def get_horasTrabalhadas(self):
        return self.__horasTrabalhadas

    def get_PontoTrabalho(self):
        return {
            'dataRegistro': self.get_dataRegistro(),
            'horaChegada': self.get_horaChegada(),
            'horaSaida': self.get_horaSaida(),
            'horasTrabalhadas': self.get_horasTrabalhadas()
        }
    
    def set_dataRegistro(self, dataRegistro):
        if isinstance(dataRegistro, date):
            self.__dataRegistro = dataRegistro
            return True
        return False
    
    def set_horaChegada(self, horaChegada):
        if isinstance(horaChegada, time):
            self.__horaChegada = horaChegada
            return True
        return False
    
    def set_horaSaida(self, horaSaida):
        if isinstance(horaSaida, time):
            self.__horaSaida = horaSaida
            return True
        return False
    
    def set_horasTrabalhadas(self, horasTrabalhadas):
        if isinstance(horasTrabalhadas, (int, float)) and horasTrabalhadas >= 0:
            self.__horasTrabalhadas = horasTrabalhadas
            return True
        return False