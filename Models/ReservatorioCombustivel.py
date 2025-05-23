from conexao import Conexao
from mysql.connector import Error

class ReservatorioModel:
    @staticmethod
    def set_reservatorio(capacidade, nivel, temperatura, idCombustivel):
        """Cadastra um novo reservatório no banco"""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            query = """
                INSERT INTO reservatorio (capacidade, nivel, temperatura, idcombustivel)
                VALUES (%s, %s, %s, %s)
            """
            valores = (capacidade, nivel, temperatura, idCombustivel)

            cursor.execute(query, valores)
            conexao.commit()

            return True  # Cadastro realizado com sucesso

        except Exception as e:
            print(f"Erro no Model Reservatório: {e}")
            return False

        finally:
            cursor.close()
            conexao.close()

    @staticmethod
    def get_reservatorio():
        """Lista todos os reservatórios cadastrados com o nome do combustível"""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            # Realiza um JOIN para obter o nome do combustível a partir da tabela combustivel
            query = """
                SELECT r.idreservatorio, c.nome, r.capacidade, r.nivel, r.temperatura
                FROM reservatorio r
                JOIN combustivel c ON r.idcombustivel = c.idcombustivel
            """
            cursor.execute(query)
            reservatorios = cursor.fetchall()

            lista_reservatorios = [
                {
                    "id": reservatorio[0],
                    "combustivel": reservatorio[1],  # Nome do combustível
                    "capacidade": float(reservatorio[2]),
                    "nivelAtual": float(reservatorio[3]),
                    "temperatura": float(reservatorio[4])
                }
                for reservatorio in reservatorios
            ]

            return lista_reservatorios
        except Error as err:
            print(f"MODEL: Erro ao listar reservatórios: {err}")
            return None
        finally:
            cursor.close()
            conexao.close()

    @staticmethod
    def update_reservatorio(idReservatorio, capacidade, nivel, temperatura, idCombustivel):
        """Atualiza os dados de um reservatório existente."""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()
            query = """
                UPDATE reservatorio
                SET capacidade = %s, nivel = %s, temperatura = %s, idcombustivel = %s
                WHERE idReservatorio = %s
            """
            valores = (capacidade, nivel, temperatura, idCombustivel, idReservatorio)
            cursor.execute(query, valores)
            conexao.commit()

            # Verifica se alguma linha foi afetada
            return cursor.rowcount > 0

        except Exception as e:
            print(f"Erro ao atualizar reservatório: {e}")
            return False

        finally:
            cursor.close()
            conexao.close()


    @staticmethod
    def delete_reservatorio(idReservatorio):
        """Deleta um reservatório a partir do seu ID."""
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()
            query = "DELETE FROM reservatorio WHERE idReservatorio = %s"
            cursor.execute(query, (idReservatorio,))
            conexao.commit()

            # Verifica se a exclusão afetou alguma linha
            return cursor.rowcount > 0

        except Exception as e:
            print(f"Erro ao deletar reservatório: {e}")
            return False

        finally:
            cursor.close()
            conexao.close()