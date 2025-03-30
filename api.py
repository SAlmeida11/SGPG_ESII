from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from conexao import Conexao
from Controller.CtrCombustivel import CombustivelController
from Controller.CtrGerenciarReservatorio import ReservatorioController

app = Flask(__name__)
#CORS(app) #Permite solicitações
CORS(app, origins=["http://localhost:3000"])
#Permite solicitações apenas da origin específica

combustivel_bp = Blueprint("combustivel", __name__)
reservatorio_bp = Blueprint("reservatorio", __name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"  # Altere conforme necessário
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response

# Rota para listar funcionários
@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    conexao = Conexao.criar_conexao()
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

#Rota para buscar funcionario
@app.route('/funcionarios/<cpf>', methods=['GET'])
def buscar_funcionario(cpf):
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        # Consulta SQL para buscar o funcionário pelo CPF
        query = """
            SELECT nomeFun, cpf, admin, dtNascimento, vinculo_id_vinculo, endereco_id_endereco
            FROM funcionario
            WHERE cpf = %s
        """
        cursor.execute(query, (cpf,))
        funcionario = cursor.fetchone()

        # Se o funcionário não for encontrado, retorna 404
        if funcionario is None:
            return jsonify({"erro": "Funcionário não encontrado"}), 404

        # Convertendo os dados para um formato JSON adequado
        funcionario_data = {
            "nomeFun": funcionario[0],
            "cpf": funcionario[1],
            "admin": funcionario[2],
            "dtNascimento": funcionario[3],
            "vinculo_id_vinculo": funcionario[4],
            "endereco_id_endereco": funcionario[5]
        }

        return jsonify(funcionario_data), 200

    except Error as err:
        print(f"Erro ao buscar o funcionário: {err}")
        return jsonify({"erro": "Erro ao buscar o funcionário"}), 500

    finally:
        cursor.close()
        conexao.close()        

# Rota para adicionar um funcionário
@app.route('/cadfuncionarios', methods=['POST'])
def adicionar_funcionario():
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        # Obtendo os dados do corpo da requisição
        dados = request.json

        #Tabela Vinculo
        id_endereco = 7 #dados.get("id_endereco")
        logradouro = dados.get("logradouro")
        numero = dados.get("numero")
        bairro = "Brooklyn"#dados.get("bairro")
        cidade = dados.get("cidade")
        estado = dados.get("estado")
        cep = dados.get("cep")

        #Tabela Endereco
        id_vinculo = 'V010'#dados.get("id_vinculo")
        dtContratacao = dados.get("dtContratacao")
        salario = dados.get("salario")
        status = 1 #dados.get("status")

        #Tabela Funcionario
        nomeFun = dados.get("nome")
        cpf = dados.get("cpf")
        dtNascimento = dados.get("dataNascimento")
        admin = 0#int(dados.get("admin", 0))  # Considera 0 como padrão para admin

        # Validação dos dados recebidos
        if not nomeFun or not cpf or not dtNascimento:
            return jsonify({"erro": "Dados incompletos"}), 400

        query = """
            START TRANSACTION;

            -- 1. Inserir um endereço
            INSERT INTO endereco (id_endereco, logradouro, numero, bairro, cidade, estado, cep)
            VALUES (%s, %s, %s, %s, %s, %s, %s);

            -- 2. Inserir um vínculo empregatício
            INSERT INTO vinculo (id_vinculo, dtContratacao, salario, status)
            VALUES (%s, %s, %s, %s);

            -- 3. Inserir o funcionário
            INSERT INTO funcionario (nomeFun, dtNascimento, cpf, admin, vinculo_id_vinculo, endereco_id_endereco)
            VALUES (%s, %s, %s, %s);

            -- Se tudo der certo, confirma a transação
            COMMIT;
        """
        cursor.execute(query, (id_endereco, logradouro, numero, bairro, cidade, estado, cep, id_vinculo, dtContratacao, salario, status, nomeFun, cpf, dtNascimento, admin))
        conexao.commit()

        return jsonify({"mensagem": "Funcionário cadastrado com sucesso!", "id": cursor.lastrowid}), 201
    except Error as err:
        conexao.rollback()
        print(f"Erro ao adicionar funcionário: {err}")
        return jsonify({"erro": "Erro ao cadastrar funcionário"}), 500
    finally:
        cursor.close()
        conexao.close()

# Rota para listar clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        query = "SELECT cpf, nomeCliente, tipo, dataCadastro, endereco_id_endereco FROM cliente"
        cursor.execute(query)
        clientes = cursor.fetchall()

        # Convertendo os dados para um formato JSON adequado
        lista_clientes = [
            {
                "cpf": cliente[0],
                "nomeCliente": cliente[1],
                "tipo": cliente[2],
                "dataCadastro": cliente[3],
                "endereco_id_endereco": cliente[4]
            }
            for cliente in clientes
        ]

        return jsonify(lista_clientes), 200
    except Error as err:
        print(f"Erro ao listar clientes: {err}")
        return jsonify({"erro": "Erro ao listar clientes"}), 500
    finally:
        cursor.close()
        conexao.close()

# Rota para adicionar um cliente
@app.route('/clientes', methods=['POST'])
def adicionar_cliente():
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        # Obtendo os dados do corpo da requisição
        dados = request.json
        cpf = dados.get("cpf")
        nomeCliente = dados.get("nomeCliente")
        tipo = dados.get("tipo")
        dataCadastro = dados.get("dataCadastro")
        endereco_id_endereco = dados.get("endereco_id_endereco")

        # Validação dos dados recebidos
        if not cpf or not nomeCliente or not tipo or not dataCadastro or not endereco_id_endereco:
            return jsonify({"erro": "Dados incompletos"}), 400

        query = """
            INSERT INTO cliente 
            (cpf, nomeCliente, tipo, dataCadastro, endereco_id_endereco)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (cpf, nomeCliente, tipo, dataCadastro, endereco_id_endereco))
        conexao.commit()

        return jsonify({"mensagem": "Cliente cadastrado com sucesso!", "id": cursor.lastrowid}), 201
    except Error as err:
        conexao.rollback()
        print(f"Erro ao adicionar cliente: {err}")
        return jsonify({"erro": "Erro ao cadastrar cliente"}), 500
    finally:
        cursor.close()
        conexao.close()

# Rota para listar fornecedores
@app.route('/fornecedores', methods=['GET'])
def listar_fornecedores():
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        query = "SELECT cnpj, NomeFor, Encarregado, Status, produtosFornecidos, funcionario_cpf FROM fornecedor"
        cursor.execute(query)
        fornecedores = cursor.fetchall()

        # Convertendo os dados para um formato JSON adequado
        lista_fornecedores = [
            {
                "cnpj": fornecedor[0],
                "NomeFor": fornecedor[1],
                "Encarregado": fornecedor[2],
                "Status": fornecedor[3],
                "produtosFornecidos": fornecedor[4],
                "funcionario_cpf": fornecedor[5]
            }
            for fornecedor in fornecedores
        ]

        return jsonify(lista_fornecedores), 200
    except Error as err:
        print(f"Erro ao listar fornecedores: {err}")
        return jsonify({"erro": "Erro ao listar fornecedores"}), 500
    finally:
        cursor.close()
        conexao.close()

@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    cpf = dados.get("cpf")
    senha = dados.get("senha")

    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        query = "SELECT cpf FROM funcionario WHERE cpf = %s"
        cursor.execute(query, (cpf,))
        usuario = cursor.fetchone()

        if usuario and usuario[0] == cpf and senha == cpf:
            return jsonify({"mensagem": "Login bem-sucedido"}), 200
        else:
            return jsonify({"erro": "CPF ou senha incorretos"}), 401
    except Error as err:
        print(f"Erro ao realizar login: {err}")
        return jsonify({"erro": "Erro interno no servidor"}), 500
    finally:
        cursor.close()
        conexao.close()

@combustivel_bp.route("/combustiveis", methods=["POST"])
def cadastrar_combustivel():
    #Rota para cadastrar um novo combustível
    dados = request.json
    resposta, status = CombustivelController.cadastrar_combustivel(dados)
    return jsonify(resposta), status

@combustivel_bp.route("/combustiveis", methods=["GET"])
def listar_combustiveis():
    #Rota para listar todos os combustíveis
    resposta, status = CombustivelController.listar_combustiveis()
    return jsonify(resposta), status   

app.register_blueprint(combustivel_bp)

@reservatorio_bp.route("/reservatorios", methods=["POST"])
def cadastrar_reservatorio():
    dados = request.json
    resposta, status = ReservatorioController.cadastrar_reservatorio(dados)
    return jsonify(resposta), status

@reservatorio_bp.route("/reservatorios", methods=["GET"])
def listar_reservatorios():
    resposta, status = ReservatorioController.listar_reservatorios()
    return jsonify(resposta), status

app.register_blueprint(reservatorio_bp)

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