class Combustivel():
    def __init__(self, nome: str, preco_litro: float, categoria: str, qtd_disponivel: float):
        self.__nome = nome
        self.__preco_litro = self.__validar_preco(preco_litro)
        self.__categoria = categoria
        self.__qtd_disponivel = self.__validar_qtdDisp(qtd_disponivel)
    
    def __validar_preco(self, preco):
        if isinstance(preco, float):
            return preco
        else:
            raise ValueError("Preco invalido.")
    
    def __validar_qtdDisp(self, qtd):
        if isinstance(qtd, float):
            return qtd
        else:
            raise ValueError("Quantidade de combustivel invalida.")
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_preco_litro(self):
        return self.__preco_litro
    
    def set_preco_litro(self, preco):
        self.__preco_litro = self.__validar_preco(preco)
    
    def get_categoria(self):
        return self.__categoria
    
    def set_categoria(self, categoria):
        self.__categoria = categoria
    
    def get_qtd_disponivel(self):
        return self.__qtd_disponivel
    
    def set_qtd_disponivel(self, qtd):
        self.__qtd_disponivel = self.__validar_qtdDisp(qtd)
