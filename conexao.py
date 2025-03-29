import mysql.connector
from mysql.connector import Error

class Conexao:
    # Função para conectar ao banco de dados
    def criar_conexao():
        try:
            conexao = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="sua_senha",
                database="mydb"
            )
            if conexao.is_connected():
                return conexao
        except Error as e:
            print(f"Erro de conexão ao banco de dados: {e}")
            return None

