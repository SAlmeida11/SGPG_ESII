from Models.Teste import OrdemServicoModel, ClienteModel, ServicoModel
from datetime import datetime

class OrdemServicoController:
    def __init__(self):
        self.model = OrdemServicoModel()
        self.cliente_model = ClienteModel()
        self.servico_model = ServicoModel()

    def cadastrar_ordem_servico(self, ordem_servico):
        """Registra uma nova ordem de serviço"""
        try:
            return self.model.adicionar_ordem_servico(ordem_servico)
        except Exception as e:
            print(f"Erro ao cadastrar ordem de serviço: {str(e)}")
            raise

    def adicionar_servico(self, servico, ordem_servico_id):
        """Adiciona um serviço a uma ordem de serviço"""
        try:
            return self.model.adicionar_servico(ordem_servico_id, servico)
        except Exception as e:
            print(f"Erro ao adicionar serviço: {str(e)}")
            raise

    def remover_servico(self, servico_id, ordem_servico_id):
        """Remove um serviço de uma ordem de serviço"""
        try:
            return self.model.remover_servico(ordem_servico_id, servico_id)
        except Exception as e:
            print(f"Erro ao remover serviço: {str(e)}")
            raise

    def consultar_preco(self, ordem_servico_id):
        """Consulta o preço total de uma ordem de serviço"""
        try:
            return self.model.calcular_preco(ordem_servico_id)
        except Exception as e:
            print(f"Erro ao consultar preço: {str(e)}")
            return 0.0

    def buscar_cliente(self, cliente_id):
        """Busca um cliente pelo ID"""
        try:
            return self.cliente_model.buscar_cliente(cliente_id)
        except Exception as e:
            print(f"Erro ao buscar cliente: {str(e)}")
            return None

    def fechar(self):
        """Libera recursos da conexão"""
        self.model.fechar_conexao()
        self.cliente_model.fechar_conexao()
        self.servico_model.fechar_conexao()
