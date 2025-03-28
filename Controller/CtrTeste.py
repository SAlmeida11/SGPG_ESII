from Models.Teste import FuncionarioModel
from datetime import datetime

class FuncionarioController:
    def __init__(self):
        self.model = FuncionarioModel()

    def obter_lista_funcionarios(self):
        """Retorna todos os funcionários formatados para a view"""
        try:
            funcionarios = self.model.listar_funcionarios()
            # Como estamos usando dictionary=True, não precisa converter
            return funcionarios
        except Exception as e:
            print(f"Erro ao obter funcionários: {str(e)}")
            return []
        finally:
            self.model.fechar_conexao()

    def criar_funcionario(self, nomeFun, cpf, dtNascimento, admin, vinculo_id_vinculo, endereco_id_endereco):
        """Valida e cria um novo funcionário"""
        try:
            if not self._validar_cpf(cpf):
                raise ValueError("CPF inválido")
                
            if not self._validar_data(dtNascimento):
                raise ValueError("Data de nascimento inválida")
                
            return self.model.adicionar_funcionario(
                nomeFun, cpf, dtNascimento, admin, 
                vinculo_id_vinculo, endereco_id_endereco
            )
        except Exception as e:
            print(f"Erro ao criar funcionário: {str(e)}")
            raise  # Re-lança a exceção para ser tratada pela view

    def editar_funcionario(self, cpf, nomeFun, admin, vinculo_id_vinculo, endereco_id_endereco):
        """Atualiza os dados de um funcionário existente"""
        try:
            if not self._validar_cpf(cpf):
                raise ValueError("CPF inválido")
                
            return self.model.atualizar_funcionario(
                cpf, nomeFun, admin, vinculo_id_vinculo, endereco_id_endereco
            )
        except Exception as e:
            print(f"Erro ao editar funcionário: {str(e)}")
            raise

    def deletar_funcionario(self, cpf):
        """Remove um funcionário pelo CPF"""
        try:
            if not self._validar_cpf(cpf):
                raise ValueError("CPF inválido")
                
            return self.model.excluir_funcionario(cpf)
        except Exception as e:
            print(f"Erro ao deletar funcionário: {str(e)}")
            raise

    # Métodos auxiliares de validação
    def _validar_cpf(self, cpf):
        """Validação básica de CPF (pode ser implementada completa depois)"""
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