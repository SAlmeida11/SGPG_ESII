from conexao import Conexao
from mysql.connector import Error

class ItemModel:
    @staticmethod
    def set_item(NomeItem, Categoria, QtdeEstoque, PrecUnitario, CodigoBarras, funcionario_cpf):
        """Cadastra um novo item no banco"""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            query = """
                INSERT INTO item (NomeItem, Categoria, QtdeEstoque, PrecUnitario, CodigoBarras, funcionario_cpf)  
                VALUES  (%s, %s, %s, %s, %s, %s)
            """
            valores = (NomeItem, Categoria, QtdeEstoque, PrecUnitario, CodigoBarras, funcionario_cpf)

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
    def get_Item():
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        try:
            query = "SELECT NomeItem, Categoria, QtdeEstoque, PrecUnitario, CodigoBarras, funcionario_cpf FROM item"
            cursor.execute(query)
            itens = cursor.fetchall()

            lista_itens = [
                {
                    "nome": item[0],
                    "categoria": item[1],
                    "quantidade_disponivel": item[2],
                    "preco_unitario": item[3],
                    "codigo_barras": item[4],
                    "funcionario_cpf": item[5]
                }
                for item in itens
            ]

            return lista_itens
        except Error as err:
            print(f"MODEL: Erro ao listar itens: {err}")
            # Em vez de retornar um Response, retorne um valor padrão ou levante a exceção
            return None
        finally:
            cursor.close()
            conexao.close()
