from conexao import Conexao
from mysql.connector import Error

class PagamentoModel:
    @staticmethod
    def set_pagamento(Valor, FormaPagamento, Parcelado, Desconto, Juros, IntituiicaoCartaoCred_cnpj):
        """Cadastra um novo pagamento no banco"""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            query = """
                INSERT INTO pagamento (Valor, FormaPagamento, Parcelado, Desconto, Juros, InstituiicaoCartaoCred_cnpj)  
                VALUES  (%s, %s, %s, %s, %s, %s)
            """
            valores = (Valor, FormaPagamento, Parcelado, Desconto, Juros, IntituiicaoCartaoCred_cnpj)

            cursor.execute(query, valores)
            conexao.commit()

            return True  # Cadastro realizado com sucesso

        except Exception as e:
            print(f"Erro no Model: {e}")
            return False

        finally:
            cursor.close()
            conexao.close()

    @staticmethod
    def get_pagamento():
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        try:
            query = "SELECT id_pagamento, Valor, FormaPagamento, Parcelado, Desconto, Juros, InstituiicaoCartaoCred_cnpj FROM pagamento"
            cursor.execute(query)
            pagamentos = cursor.fetchall()

            lista_pagamentos = [
                {
                    "id_pagamento": pagamento[0],
                    "Valor": pagamento[1],
                    "FormaPagamento": pagamento[2],
                    "Parcelado": pagamento[3],
                    "Desconto": pagamento[4],
                    "Juros": pagamento[5],
                    "IntituiicaoCartaoCred_cnpj": pagamento[6]
                }
                for pagamento in pagamentos
            ]

            return lista_pagamentos
        except Error as err:
            print(f"MODEL: Erro ao listar pagamentos: {err}")
            # Em vez de retornar um Response, retorne um valor padrão ou levante a exceção
            return None
        finally:
            cursor.close()
            conexao.close()




# class Pagamento:
#     def __init__(self, valor: float, forma_pagamento: str, parcelado: bool, desconto: float = 0.0, juros: float = 0.0):
#         self._valor = valor
#         self._forma_pagamento = forma_pagamento
#         self._parcelado = parcelado
#         self._desconto = desconto
#         self._juros = juros

#     def get_valor(self):
#         return self._valor

#     def set_valor(self, valor: float):
#         self._valor = valor

#     def get_forma_pagamento(self):
#         return self._forma_pagamento

#     def set_forma_pagamento(self, forma_pagamento: str):
#         self._forma_pagamento = forma_pagamento

#     def get_parcelado(self):
#         return self._parcelado

#     def set_parcelado(self, parcelado: bool):
#         self._parcelado = parcelado

#     def get_desconto(self):
#         return self._desconto

#     def set_desconto(self, desconto: float):
#         self._desconto = desconto

#     def get_juros(self):
#         return self._juros

#     def set_juros(self, juros: float):
#         self._juros = juros
