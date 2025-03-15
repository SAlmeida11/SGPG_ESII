class Endereco:
    def __init__(self, logradouro, numero, bairro, cidade, estado, cep):
        self._logradouro = logradouro
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._cep = cep
    
    def get_logradouro(self):
        return self._logradouro
    
    def set_logradouro(self, logradouro):
        self._logradouro = logradouro
    
    def get_numero(self):
        return self._numero
    
    def set_numero(self, numero):
        self._numero = numero
    
    def get_bairro(self):
        return self._bairro
    
    def set_bairro(self, bairro):
        self._bairro = bairro
    
    def get_cidade(self):
        return self._cidade
    
    def set_cidade(self, cidade):
        self._cidade = cidade
    
    def get_estado(self):
        return self._estado
    
    def set_estado(self, estado):
        self._estado = estado
    
    def get_cep(self):
        return self._cep
    
    def set_cep(self, cep):
        self._cep = cep

    #def atualizarEndereco(endereco):
        