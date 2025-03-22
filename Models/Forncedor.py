class Fornecedor:
    def __init__(self, nome_for, cnpj, encarregado, status, produtos_fornecidos):
        self._nome_for = nome_for
        self._cnpj = cnpj
        self._encarregado = encarregado
        self._status = status
        self._produtos_fornecidos = set(produtos_fornecidos)
    
    def get_nome_for(self):
        return self._nome_for
    
    def set_nome_for(self, nome_for):
        self._nome_for = nome_for
    
    def get_cnpj(self):
        return self._cnpj
    
    def set_cnpj(self, cnpj):
        self._cnpj = cnpj
    
    def get_encarregado(self):
        return self._encarregado
    
    def set_encarregado(self, encarregado):
        self._encarregado = encarregado
    
    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status
    
    def get_produtos_fornecidos(self):
        return self._produtos_fornecidos
    
    def set_produtos_fornecidos(self, produtos_fornecidos):
        self._produtos_fornecidos = set(produtos_fornecidos)
    
    def add_produto(self, produto):
        self._produtos_fornecidos.add(produto)
    
    def remove_produto(self, produto):
        self._produtos_fornecidos.discard(produto)
