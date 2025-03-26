import mysql.connector

class FuncionarioModel:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="sua_senha",
            database="db_sgpg"
        )
        self.cursor = self.conexao.cursor()

    def listar_funcionarios(self):
        query = "SELECT nome, telefone, cpf, status FROM Funcionario"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def adicionar_funcionario(self, nome, telefone, cpf, status):
        query = "INSERT INTO Funcionario (nome, telefone, cpf, status) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (nome, telefone, cpf, status))
        self.conexao.commit()

    def atualizar_funcionario(self, id_funcionario, nome, telefone, cpf, status):
        query = "UPDATE Funcionario SET nome=%s, telefone=%s, cpf=%s, status=%s WHERE id=%s"
        self.cursor.execute(query, (nome, telefone, cpf, status, id_funcionario))
        self.conexao.commit()

    def excluir_funcionario(self, id_funcionario):
        query = "DELETE FROM Funcionario WHERE id=%s"
        self.cursor.execute(query, (id_funcionario,))
        self.conexao.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
