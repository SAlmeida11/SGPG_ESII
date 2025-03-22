class Contato:
    def __init__(self, ddd, telefone, email):
        self._ddd = ddd
        self._telefone = telefone
        self._email = email
    
    def get_ddd(self):
        return self._ddd
    
    def set_ddd(self, ddd):
        self._ddd = ddd
    
    def get_telefone(self):
        return self._telefone
    
    def set_telefone(self, telefone):
        self._telefone = telefone
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email