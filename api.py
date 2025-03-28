from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app) #Permite solicitações
#CORS(app, origins=["htpp://localhost:3000"]) 
#Permite solicitações apenas da origin específica


# Função para conectar ao banco de dados
def criar_conexao():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="sua_senha",
        database="mydb"
    )

# Rota para listar funcionários
@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        query = "SELECT nomeFun, cpf, admin, dtNascimento, vinculo_id_vinculo, endereco_id_endereco FROM funcionario"
        cursor.execute(query)
        funcionarios = cursor.fetchall()

        # Convertendo os dados para um formato JSON adequado
        lista_funcionarios = [
            {
                "nomeFun": funcionario[0],
                "cpf": funcionario[1],
                "admin": funcionario[2],
                "dtNascimento": funcionario[3],
                "vinculo_id_vinculo": funcionario[4],
                "endereco_id_endereco": funcionario[5]
            }
            for funcionario in funcionarios
        ]

        return jsonify(lista_funcionarios), 200
    except Error as err:
        print(f"Erro ao listar funcionários: {err}")
        return jsonify({"erro": "Erro ao listar funcionários"}), 500
    finally:
        cursor.close()
        conexao.close()

# Rota para adicionar um funcionário
@app.route('/funcionarios', methods=['POST'])
def adicionar_funcionario():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        # Obtendo os dados do corpo da requisição
        dados = request.json
        nome = dados.get("nome")
        cpf = dados.get("cpf")
        dtNascimento = dados.get("dataNascimento")
        admin = int(dados.get("admin", 0))  # Considera 0 como padrão para admin
        vinculo_id_vinculo = dados.get("vinculo_id_vinculo")
        endereco_id_endereco = dados.get("endereco_id_endereco")

        # Validação dos dados recebidos
        if not nome or not cpf or not dtNascimento or not vinculo_id_vinculo or not endereco_id_endereco:
            return jsonify({"erro": "Dados incompletos"}), 400

        query = """
            INSERT INTO funcionario 
            (nomeFun, cpf, dtNascimento, admin, vinculo_id_vinculo, endereco_id_endereco) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nome, cpf, dtNascimento, admin, vinculo_id_vinculo, endereco_id_endereco))
        conexao.commit()

        return jsonify({"mensagem": "Funcionário cadastrado com sucesso!", "id": cursor.lastrowid}), 201
    except Error as err:
        conexao.rollback()
        print(f"Erro ao adicionar funcionário: {err}")
        return jsonify({"erro": "Erro ao cadastrar funcionário"}), 500
    finally:
        cursor.close()
        conexao.close()

if __name__ == '__main__':
    app.run(debug=True)



"""from flask import Flask, jsonify, request
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
    controller.criar_funcionario(data['nomeFun'], data['dtNascimento'], data['cpf'], data['admin'], data['vinculo_id_vinculo'], data['endereco_id_endereco'])
    return jsonify({"message": "Funcionário adicionado com sucesso!"})

@app.route('/funcionarios/<int:cpf>', methods=['PUT'])
def atualizar_funcionario(cpf):
    data = request.json
    controller.editar_funcionario(cpf, data['nomeFun'], data['dtNascimento'], data['cpf'], data['admin'])
    return jsonify({"message": "Funcionário atualizado com sucesso!"})

@app.route('/funcionarios/<int:cpf>', methods=['DELETE'])
def excluir_funcionario(cpf):
    controller.deletar_funcionario(cpf)
    return jsonify({"message": "Funcionário excluído com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
"""