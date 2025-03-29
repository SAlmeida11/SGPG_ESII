class Pagamento:
    def __init__(self, valor: float, forma_pagamento: str, parcelado: bool, desconto: float = 0.0, juros: float = 0.0):
        self._valor = valor
        self._forma_pagamento = forma_pagamento
        self._parcelado = parcelado
        self._desconto = desconto
        self._juros = juros

    def get_valor(self):
        return self._valor

    def set_valor(self, valor: float):
        self._valor = valor

    def get_forma_pagamento(self):
        return self._forma_pagamento

    def set_forma_pagamento(self, forma_pagamento: str):
        self._forma_pagamento = forma_pagamento

    def get_parcelado(self):
        return self._parcelado

    def set_parcelado(self, parcelado: bool):
        self._parcelado = parcelado

    def get_desconto(self):
        return self._desconto

    def set_desconto(self, desconto: float):
        self._desconto = desconto

    def get_juros(self):
        return self._juros

    def set_juros(self, juros: float):
        self._juros = juros
