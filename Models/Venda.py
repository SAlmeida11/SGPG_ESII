from datetime import datetime

class Venda:
    def __init__(self, data_hora: datetime):
        self._data_hora = data_hora
    
    # Getter para data_hora
    def get_data_hora(self):
        return self._data_hora
    
    # Setter para data_hora
    def set_data_hora(self, nova_data_hora):
        if isinstance(nova_data_hora, datetime):
            self._data_hora = nova_data_hora
            return True
        return False
    