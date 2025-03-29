from Models.Teste import FornecedorModel
from datetime import datetime

class FornecedorController:
    def __init__(self):
        self.model = FornecedorModel()

    def registrar_fornecedor(self, fornecedor):
        """Registra um novo fornecedor"""
        try:
            return self.model.adicionar_fornecedor(fornecedor)
        except Exception as e:
            print(f"Erro ao registrar fornecedor: {str(e)}")
            raise

    def atualizar_fornecedor(self, fornecedor):
        """Atualiza os dados de um fornecedor existente"""
        try:
            return self.model.atualizar_fornecedor(fornecedor)
        except Exception as e:
            print(f"Erro ao atualizar fornecedor: {str(e)}")
            raise

    def remover_fornecedor(self, fornecedor):
        """Remove um fornecedor"""
        try:
            return self.model.excluir_fornecedor(fornecedor)
        except Exception as e:
            print(f"Erro ao remover fornecedor: {str(e)}")
            raise

    def consultar_fornecedor(self):
        """Consulta e retorna a lista de fornecedores"""
        try:
            return self.model.listar_fornecedores()
        except Exception as e:
            print(f"Erro ao consultar fornecedores: {str(e)}")
            return []
        finally:
            self.model.fechar_conexao()

    def fechar(self):
        """Libera recursos da conexão"""
        self.model.fechar_conexao()
