from conexao import Conexao
from mysql.connector import Error

class VendaModel:
    @staticmethod
    def set_venda(data_hora, venda_combustivel_id, pagamento_id, cliente_cpf, funcionario_cpf):
        """Cadastra uma nova venda no banco"""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            query = """
                INSERT INTO venda (data_hora, Venda_combustivel_idvendaCombustivel, Pagamento_id_pagamento, cliente_cpf, funcionario_cpf)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (data_hora, venda_combustivel_id, pagamento_id, cliente_cpf, funcionario_cpf)

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
    def get_vendas():
        """Obtém todas as vendas registradas no banco"""
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        try:
            query = """
                SELECT id_venda, data_hora, Venda_combustivel_idvendaCombustivel, Pagamento_id_pagamento, cliente_cpf, funcionario_cpf
                FROM venda
            """
            cursor.execute(query)
            vendas = cursor.fetchall()

            lista_vendas = [
                {
                    "id_venda": venda[0],
                    "data_hora": venda[1],
                    "Venda_combustivel_idvendaCombustivel": venda[2],
                    "Pagamento_id_pagamento": venda[3],
                    "cliente_cpf": venda[4],
                    "funcionario_cpf": venda[5]
                }
                for venda in vendas
            ]

            return lista_vendas

        except Error as err:
            print(f"MODEL: Erro ao listar vendas: {err}")
            return None

        finally:
            cursor.close()
            conexao.close()



# from datetime import datetime

# class Venda:
#     def __init__(self, data_hora: datetime):
#         self._data_hora = data_hora
    
#     # Getter para data_hora
#     def get_data_hora(self):
#         return self._data_hora
    
#     # Setter para data_hora
#     def set_data_hora(self, nova_data_hora):
#         if isinstance(nova_data_hora, datetime):
#             self._data_hora = nova_data_hora
#             return True
#         return False
    