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
        
if __name__ == "__main__":
    try:
        comb = VendaCombustivel("123")
        print(comb.getTipoCombustivel())
    except ValueError as e:
        print(f"Erro: {e}")