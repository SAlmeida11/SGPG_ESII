from flask import Flask, jsonify, request
from Controller.CtrTeste import FuncionarioController

app = Flask(__name__)
controller = FuncionarioController()

@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    funcionarios = controller.obter_lista_funcionarios()
    return jsonify(funcionarios)

@app.route('/funcionarios', methods=['POST'])
def adicionar_funcionario():
    data = request.json
    controller.criar_funcionario(data['nome'], data['telefone'], data['cpf'], data['status'])
    return jsonify({"message": "Funcionário adicionado com sucesso!"})

@app.route('/funcionarios/<int:cpf>', methods=['PUT'])
def atualizar_funcionario(cpf):
    data = request.json
    controller.editar_funcionario(cpf, data['nome'], data['telefone'], data['cpf'], data['status'])
    return jsonify({"message": "Funcionário atualizado com sucesso!"})

@app.route('/funcionarios/<int:cpf>', methods=['DELETE'])
def excluir_funcionario(cpf):
    controller.deletar_funcionario(cpf)
    return jsonify({"message": "Funcionário excluído com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
