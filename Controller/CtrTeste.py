from Models.Teste import FuncionarioModel

class FuncionarioController:
    def __init__(self):
        self.model = FuncionarioModel()

    def obter_lista_funcionarios(self):
        funcionarios = self.model.listar_funcionarios()
        return [{"nome": f[0], "telefone": f[1], "cpf": f[2], "status": f[3]} for f in funcionarios]

    def criar_funcionario(self, nome, telefone, cpf, status):
        self.model.adicionar_funcionario(nome, telefone, status)

    def editar_funcionario(self, nome, telefone, cpf, status):
        self.model.atualizar_funcionario( nome, telefone, cpf, status)

    def deletar_funcionario(self, cpf):
        self.model.excluir_funcionario(cpf)

    def fechar(self):
        self.model.fechar_conexao()
