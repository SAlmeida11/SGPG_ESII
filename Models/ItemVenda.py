class ItemVenda:
    def __init__(self, quantidade):
        self._quantidade = quantidade

    def get_quantidade(self):
        return self._quantidade
    
    def set_quantidade(self, quantidade):
        if (quantidade > 0):
            self._quantidade = quantidade
        else:
            raise ValueError("Valor inválido.")