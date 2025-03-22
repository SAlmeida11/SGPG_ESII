class VendaCombustivel:
    def __init__(self, tipoCombustivel):
        self.setTipoCombustivel(tipoCombustivel)

    def getTipoCombustivel(self):
        return self.__tipoCombustivel
    
    def setTipoCombustivel(self, novoTipoCombustivel):
        if isinstance(novoTipoCombustivel, str) and len(novoTipoCombustivel) > 0:
            self.__tipoCombustivel = novoTipoCombustivel
        else:
            raise ValueError("Tipo de combustível incorreto.")