from conexao import Conexao
from mysql.connector import Error

class ClienteModel:
    @staticmethod
    def set_cliente(logradouro, numero, bairro, cidade, estado, cep, cpf, nome, tipo, dataCadastro):
        """Cadastra um novo cliente no banco"""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

                        # Inserir endereço
            endereco_query = """
                INSERT INTO endereco (logradouro, numero, bairro, cidade, estado, cep) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            endereco_valores = (logradouro, numero, bairro, cidade, estado, cep)
            cursor.execute(endereco_query, endereco_valores)
            conexao.commit()
            
            # Recuperar ID do endereço recém-cadastrado
            endereco_id = cursor.lastrowid
            
            # Inserir cliente com o ID do endereço
            cliente_query = """
                INSERT INTO cliente (cpf, nome, tipo, dataCadastro, endereco_id)
                VALUES (%s, %s, %s, %s, %s)
            """
            cliente_valores = (cpf, nome, tipo, dataCadastro, endereco_id)
            cursor.execute(cliente_query, cliente_valores)
            conexao.commit()

            return True  # Cadastro realizado com sucesso

        except Exception as e:
            print(f"Erro no Model: {e}")
            return False

        finally:
            cursor.close()
            conexao.close()

    @staticmethod
    def get_cliente():
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        try:
            query = "SELECT cpf, nome, dataCadastro FROM cliente"
            cursor.execute(query)
            clientes = cursor.fetchall()

            lista_clientes = [
                {
                    "cpf": cliente[0],
                    "nome": cliente[1],
                    "dataCadastro": cliente[2]
                }
                for cliente in clientes
            ]

            return lista_clientes
        except Error as err:
            print(f"MODEL: Erro ao listar clientes: {err}")
            # Em vez de retornar um Response, retorne um valor padrão ou levante a exceção
            return None
        finally:
            cursor.close()
            conexao.close()

