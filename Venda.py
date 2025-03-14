from datetime import date, datetime

class Venda:
    def __init__(self, data_hora: datetime):
        self.data_hora = data_hora
    
    def get_venda(self):
        return self
    
    def set_venda(self, nova_venda):
        if isinstance(nova_venda, Venda):
            self.data_hora = nova_venda.data_hora
            return True
        return False
