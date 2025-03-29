from Models.Teste import ClienteModel
from datetime import datetime

class ClienteController:
    def __init__(self):
        self.model = ClienteModel()

    def obter_lista_clientes(self):
        """Retorna todos os clientes formatados para a view"""
        try:
            clientes = self.model.listar_clientes()
            return clientes
        except Exception as e:
            print(f"Erro ao obter clientes: {str(e)}")
            return []
        finally:
            self.model.fechar_conexao()

    def criar_cliente(self, nome, cpf, dtNascimento, email, telefone, endereco_id):
        """Valida e cria um novo cliente"""
        try:
            if not self._validar_cpf(cpf):
                raise ValueError("CPF inválido")
            
            if not self._validar_data(dtNascimento):
                raise ValueError("Data de nascimento inválida")
            
            return self.model.adicionar_cliente(
                nome, cpf, dtNascimento, email, telefone, endereco_id
            )
        except Exception as e:
            print(f"Erro ao criar cliente: {str(e)}")
            raise

    def editar_cliente(self, cpf, nome, email, telefone, endereco_id):
        """Atualiza os dados de um cliente existente"""
        try:
            if not self._validar_cpf(cpf):
                raise ValueError("CPF inválido")
                
            return self.model.atualizar_cliente(
                cpf, nome, email, telefone, endereco_id
            )
        except Exception as e:
            print(f"Erro ao editar cliente: {str(e)}")
            raise

    def deletar_cliente(self, cpf):
        """Remove um cliente pelo CPF"""
        try:
            if not self._validar_cpf(cpf):
                raise ValueError("CPF inválido")
                
            return self.model.excluir_cliente(cpf)
        except Exception as e:
            print(f"Erro ao deletar cliente: {str(e)}")
            raise

    # Métodos auxiliares de validação
    def _validar_cpf(self, cpf):
        """Validação básica de CPF"""
        return isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit()

    def _validar_data(self, data):
        """Valida se a data está em um formato aceitável"""
        try:
            datetime.strptime(data, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def fechar(self):
        """Libera recursos da conexão"""
        self.model.fechar_conexao()
