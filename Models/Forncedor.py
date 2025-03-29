import mysql.connector

class FornecedorModel:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="seu_usuario",
            password="sua_senha",
            database="seu_banco"
        )
        self.cursor = self.conexao.cursor(dictionary=True)

    def adicionar_fornecedor(self, fornecedor):
        """Insere um novo fornecedor no banco de dados"""
        try:
            sql = """INSERT INTO fornecedores (nome, cnpj, endereco, telefone, email)
                     VALUES (%s, %s, %s, %s, %s)"""
            valores = (fornecedor.nome, fornecedor.cnpj, fornecedor.endereco, fornecedor.telefone, fornecedor.email)
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao adicionar fornecedor: {str(e)}")
            return False

    def atualizar_fornecedor(self, fornecedor):
        """Atualiza os dados de um fornecedor existente"""
        try:
            sql = """UPDATE fornecedores SET nome=%s, endereco=%s, telefone=%s, email=%s
                     WHERE cnpj=%s"""
            valores = (fornecedor.nome, fornecedor.endereco, fornecedor.telefone, fornecedor.email, fornecedor.cnpj)
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar fornecedor: {str(e)}")
            return False

    def excluir_fornecedor(self, fornecedor):
        """Remove um fornecedor do banco de dados"""
        try:
            sql = "DELETE FROM fornecedores WHERE cnpj = %s"
            self.cursor.execute(sql, (fornecedor.cnpj,))
            self.conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao excluir fornecedor: {str(e)}")
            return False

    def listar_fornecedores(self):
        """Retorna todos os fornecedores cadastrados"""
        try:
            self.cursor.execute("SELECT * FROM fornecedores")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao listar fornecedores: {str(e)}")
            return []

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados"""
        self.cursor.close()
        self.conexao.close()
