import mysql.connector
from mysql.connector import Error
from conexao import Conexao

class ServicoModel:
    def __init__(self):
        try:
            self.conexao = Conexao.criar_conexao()
            self.cursor = self.conexao.cursor(dictionary=True)
        except Error as err:
            print(f"Erro de conexão: {err}")
            raise

    def listar_servicos(self):
        try:
            query = "SELECT id, descricao, valor, duracaoEstimada, disponivel FROM servico"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as err:
            print(f"Erro ao listar serviços: {err}")
            return []

    def adicionar_servico(self, descricao, valor, duracaoEstimada, disponivel):
        try:
            query = """
                INSERT INTO servico (descricao, valor, duracaoEstimada, disponivel)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (descricao, valor, duracaoEstimada, disponivel))
            self.conexao.commit()
            return self.cursor.lastrowid
        except Error as err:
            self.conexao.rollback()
            print(f"Erro ao adicionar serviço: {err}")
            raise

    def remover_servico(self, servico_id):
        try:
            query = "DELETE FROM servico WHERE id = %s"
            self.cursor.execute(query, (servico_id,))
            self.conexao.commit()
            return self.cursor.rowcount > 0
        except Error as err:
            self.conexao.rollback()
            print(f"Erro ao remover serviço: {err}")
            raise

    def atualizar_servico(self, servico_id, descricao, valor, duracaoEstimada, disponivel):
        try:
            query = """
                UPDATE servico 
                SET descricao = %s, valor = %s, duracaoEstimada = %s, disponivel = %s
                WHERE id = %s
            """
            self.cursor.execute(query, (descricao, valor, duracaoEstimada, disponivel, servico_id))
            self.conexao.commit()
            return self.cursor.rowcount > 0
        except Error as err:
            self.conexao.rollback()
            print(f"Erro ao atualizar serviço: {err}")
            raise

    def buscar_servico(self, servico_id):
        try:
            query = "SELECT * FROM servico WHERE id = %s"
            self.cursor.execute(query, (servico_id,))
            return self.cursor.fetchone()
        except Error as err:
            print(f"Erro ao buscar serviço: {err}")
            return None

    def __del__(self):
        if hasattr(self, 'conexao') and self.conexao.is_connected():
            self.cursor.close()
            self.conexao.close()
