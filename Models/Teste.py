import mysql.connector
from mysql.connector import Error
from conexao import Conexao

class FuncionarioModel:
    def __init__(self):
        try:
            self.conexao = Conexao.criar_conexao()
            self.cursor = self.conexao.cursor(dictionary=True)
        except Error as err:
            print(f"Erro de conexão: {err}")
            raise

    def listar_funcionarios(self):
        try:
            query = """
                SELECT nomeFun, cpf, admin, dtNascimento, 
                       vinculo_id_vinculo, endereco_id_endereco 
                FROM funcionario
            """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as err:
            print(f"Erro ao listar: {err}")
            return []

    def adicionar_funcionario(self, nome, cpf, dtNascimento, admin, vinculo_id, endereco_id):
        try:
            query = """
                INSERT INTO funcionario 
                (nomeFun, cpf, dtNascimento, admin, vinculo_id_vinculo, endereco_id_endereco) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (nome, cpf, dtNascimento, admin, vinculo_id, endereco_id))
            self.conexao.commit()
            return self.cursor.lastrowid
        except Error as err:
            self.conexao.rollback()
            print(f"Erro ao adicionar: {err}")
            raise

    # Implementar os outros métodos com o mesmo padrão...

    def __del__(self):
        if hasattr(self, 'conexao') and self.conexao.is_connected():
            self.cursor.close()
            self.conexao.close()