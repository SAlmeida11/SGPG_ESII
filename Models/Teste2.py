import mysql.connector

class FuncionarioModel:
    def __init__(self):
        # Conectando ao banco de dados
        self.conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="sua_senha",  # Substitua com sua senha
            database="mydb"  # Certifique-se de que o banco de dados seja 'mydb'
        )
        #self.cursor = self.conexao.cursor()
        # Configurar o cursor para retornar dicionários
        self.cursor = self.conexao.cursor(dictionary=True)  # <--- Adicione dictionary=True

    def listar_funcionarios(self):
        # Selecionando as colunas corretas da tabela funcionario
        query = """
            SELECT nomeFun, cpf, admin, dtNascimento, vinculo_id_vinculo, endereco_id_endereco 
            FROM funcionario
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def adicionar_funcionario(self, nome, cpf, dtNascimento, admin, vinculo_id_vinculo, endereco_id_endereco):
        # Inserir um novo funcionário na tabela 'funcionario'
        query = """
            INSERT INTO funcionario (nomeFun, cpf, dtNascimento, admin, vinculo_id_vinculo, endereco_id_endereco) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (nome, cpf, dtNascimento, admin, vinculo_id_vinculo, endereco_id_endereco))
        self.conexao.commit()

    def atualizar_funcionario(self, cpf, nome, admin, vinculo_id_vinculo, endereco_id_endereco):
        # Atualizar as informações de um funcionário com base no CPF
        query = """
            UPDATE funcionario 
            SET nomeFun=%s, admin=%s, vinculo_id_vinculo=%s, endereco_id_endereco=%s 
            WHERE cpf=%s
        """
        self.cursor.execute(query, (nome, admin, vinculo_id_vinculo, endereco_id_endereco, cpf))
        self.conexao.commit()

    def excluir_funcionario(self, cpf):
        # Excluir um funcionário com base no CPF
        query = "DELETE FROM funcionario WHERE cpf=%s"
        self.cursor.execute(query, (cpf,))
        self.conexao.commit()

    def fechar_conexao(self):
        # Fechar a conexão com o banco de dados
        self.cursor.close()
        self.conexao.close()



"""import mysql.connector

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
"""