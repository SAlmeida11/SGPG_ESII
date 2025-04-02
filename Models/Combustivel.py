from conexao import Conexao
from mysql.connector import Error

class CombustivelModel:
    @staticmethod
    def set_combustivel(nome, preco_litro, categoria, quantidade_disponivel):
        """Cadastra um novo combustível no banco"""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            query = """
                INSERT INTO combustivel (nome, preco_litro, categoria, quantidade_disponivel)
                VALUES (%s, %s, %s, %s)
            """
            valores = (nome, preco_litro, categoria, quantidade_disponivel)

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
    def get_combustivel():
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        try:
            query = "SELECT idcombustivel, nome, categoria, preco_litro, quantidade_disponivel FROM combustivel"
            cursor.execute(query)
            combustiveis = cursor.fetchall()

            lista_combustiveis = [
                {
                    "id": combustivel[0],
                    "nome": combustivel[1],
                    "categoria": combustivel[2],
                    "preco_litro": float(combustivel[3]),
                    "quantidade_disponivel": float(combustivel[4]),
                }
                for combustivel in combustiveis
            ]

            return lista_combustiveis
        except Error as err:
            print(f"MODEL: Erro ao listar combustíveis: {err}")
            # Em vez de retornar um Response, retorne um valor padrão ou levante a exceção
            return None
        finally:
            cursor.close()
            conexao.close()
    
    @staticmethod
    def update_combustivel(idCombustivel, nome, preco_litro, categoria, quantidade_disponivel):
        """Atualiza os dados de um combustível existente"""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            query = """
                UPDATE combustivel 
                SET nome = %s, preco_litro = %s, categoria = %s, quantidade_disponivel = %s 
                WHERE idcombustivel = %s
            """
            valores = (nome, preco_litro, categoria, quantidade_disponivel, idCombustivel)
            cursor.execute(query, valores)
            conexao.commit()

            return cursor.rowcount > 0  

        except Exception as e:
            print(f"Erro ao atualizar combustível: {e}")
            return False

        finally:
            cursor.close()
            conexao.close()

    @staticmethod
    def delete_combustivel(idCombustivel):
        """Deleta um combustível a partir do seu ID"""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            query = "DELETE FROM combustivel WHERE idcombustivel = %s"
            cursor.execute(query, (idCombustivel,))
            conexao.commit()

            return cursor.rowcount > 0  

        except Exception as e:
            print(f"Erro ao deletar combustível: {e}")
            return False

        finally:
            cursor.close()
            conexao.close()
