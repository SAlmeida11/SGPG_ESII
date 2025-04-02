from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from conexao import Conexao
from Controller.CtrCliente import ClienteController
from Controller.CtrCombustivel import CombustivelController
from Controller.CtrGerenciarReservatorio import ReservatorioController
from Controller.CtrItem import ItemController
from Controller.CtrPagamento import PagamentoController
from Controller.CtrVenda import VendaController

app = Flask(__name__)
#CORS(app) #Permite solicitações
CORS(app, origins=["http://localhost:3000"])
#Permite solicitações apenas da origin específica


#Bluprints
combustivel_bp = Blueprint("combustivel", __name__)
reservatorio_bp = Blueprint("reservatorio", __name__)
cliente_bp = Blueprint("cliente", __name__)
endereco_bp = Blueprint("endereco", __name__)
item_bp = Blueprint("item", __name__)
pagamento_bp = Blueprint("pagamento", __name__)
venda_bp = Blueprint("venda", __name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"  # Altere conforme necessário
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response

#ROTAS FUNCIONARIOS
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
        # Nova consulta SQL para buscar o funcionário pelo CPF, incluindo informações de endereço e vínculo
        query = """
            SELECT f.nomeFun, f.cpf, f.dtNascimento, f.admin, 
                   e.logradouro, e.numero, e.cidade, e.estado, e.cep, 
                   v.salario, v.dtContratacao 
            FROM funcionario f
            JOIN endereco e ON e.id_endereco = f.endereco_id_endereco
            JOIN vinculo v ON v.id_vinculo = f.vinculo_id_vinculo
            WHERE f.cpf = %s
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
            "dtNascimento": funcionario[2],
            "admin": funcionario[3],
            "endereco": {
                "logradouro": funcionario[4],
                "numero": funcionario[5],
                "cidade": funcionario[6],
                "estado": funcionario[7],
                "cep": funcionario[8]
            },
            "vinculo": {
                "salario": funcionario[9],
                "dtContratacao": funcionario[10]
            }
        }

        return jsonify(funcionario_data), 200

    except Error as err:
        print(f"Erro ao buscar o funcionário: {err}")
        return jsonify({"erro": "Erro ao buscar o funcionário"}), 500

    finally:
        cursor.close()
        conexao.close()

#rota para cadastrar funcionario
@app.route('/cadfuncionarios', methods=['POST'])
def adicionar_funcionario():
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        # Obtendo os dados do corpo da requisição
        dados = request.json

        # Dados da tabela Endereco
        logradouro = dados.get("logradouro")
        numero = dados.get("numero")
        bairro = dados.get("bairro", "Brooklyn")  # Definição de valor padrão
        cidade = dados.get("cidade")
        estado = dados.get("estado")
        cep = dados.get("cep")

        # Dados da tabela Vinculo
        dtContratacao = dados.get("dtContratacao")
        salario = dados.get("salario")
        status = 1  # Definindo status padrão

        # Dados da tabela Funcionario
        nomeFun = dados.get("nome")
        cpf = dados.get("cpf")
        dtNascimento = dados.get("dataNascimento")
        admin = 0  # Definindo admin padrão como 0

        # Validação dos dados recebidos
        if not all([nomeFun, cpf, dtNascimento, logradouro, numero, cidade, estado, cep, dtContratacao, salario]):
            return jsonify({"erro": "Dados incompletos"}), 400

        # Iniciar transação
        conexao.start_transaction()

        # Inserir endereço
        query_endereco = """
            INSERT INTO endereco (logradouro, numero, bairro, cidade, estado, cep)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_endereco, (logradouro, numero, bairro, cidade, estado, cep))
        id_endereco = cursor.lastrowid  # Pega o ID gerado

        # Inserir vínculo empregatício
        query_vinculo = """
            INSERT INTO vinculo (dtContratacao, salario, status)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query_vinculo, (dtContratacao, salario, status))
        id_vinculo = cursor.lastrowid  # Pega o ID gerado

        # Inserir funcionário
        query_funcionario = """
            INSERT INTO funcionario (nomeFun, dtNascimento, cpf, admin, vinculo_id_vinculo, endereco_id_endereco)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_funcionario, (nomeFun, dtNascimento, cpf, admin, id_vinculo, id_endereco))

        # Confirmar transação
        conexao.commit()

        return jsonify({"mensagem": "Funcionário cadastrado com sucesso!", "id": cursor.lastrowid}), 201

    except Error as err:
        conexao.rollback()  # Reverte mudanças em caso de erro
        print(f"Erro ao adicionar funcionário: {err}")
        return jsonify({"erro": "Erro ao cadastrar funcionário"}), 500

    finally:
        cursor.close()
        conexao.close()

#rota para remover funcionario
@app.route('/delete-funcionario/<cpf>', methods=['DELETE'])
def remover_funcionario(cpf):
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        # Verifica se o funcionário existe
        query_verificar = "SELECT cpf FROM funcionario WHERE cpf = %s"
        cursor.execute(query_verificar, (cpf,))
        if cursor.fetchone() is None:
            return jsonify({"erro": "Funcionário não encontrado"}), 404

        # Remove o funcionário
        query_remover = "DELETE FROM funcionario WHERE cpf = %s"
        cursor.execute(query_remover, (cpf,))
        conexao.commit()

        return jsonify({"mensagem": "Funcionário removido com sucesso"}), 200

    except Error as err:
        print(f"Erro ao remover o funcionário: {err}")
        return jsonify({"erro": "Erro ao remover o funcionário"}), 500

    finally:
        cursor.close()
        conexao.close()

@app.route('/editar-funcionario/<cpf>', methods=['PUT'])
def editar_funcionario(cpf):
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()
    dados = request.json

    try:
        # Verifica se o funcionário existe
        query_verificar = "SELECT cpf FROM funcionario WHERE cpf = %s"
        cursor.execute(query_verificar, (cpf,))
        if cursor.fetchone() is None:
            return jsonify({"erro": "Funcionário não encontrado"}), 404

        # Atualiza os dados do funcionário
        query_atualizar = """
            UPDATE funcionario 
            SET nomeFun = %s, dtNascimento = %s, admin = %s 
            WHERE cpf = %s
        """
        cursor.execute(query_atualizar, (dados.get("nomeFun"), dados.get("dtNascimento"), dados.get("admin"), cpf))

        # Atualiza os dados do endereço
        query_atualizar_endereco = """
            UPDATE endereco 
            SET logradouro = %s, numero = %s, cidade = %s, estado = %s, cep = %s
            WHERE id_endereco = (SELECT endereco_id_endereco FROM funcionario WHERE cpf = %s)
        """
        cursor.execute(query_atualizar_endereco, (dados["endereco"].get("logradouro"), dados["endereco"].get("numero"), 
                                                  dados["endereco"].get("cidade"), dados["endereco"].get("estado"), 
                                                  dados["endereco"].get("cep"), cpf))

        # Atualiza os dados do vínculo
        query_atualizar_vinculo = """
            UPDATE vinculo 
            SET salario = %s, dtContratacao = %s 
            WHERE id_vinculo = (SELECT vinculo_id_vinculo FROM funcionario WHERE cpf = %s)
        """
        cursor.execute(query_atualizar_vinculo, (dados["vinculo"].get("salario"), dados["vinculo"].get("dtContratacao"), cpf))
        
        conexao.commit()

        return jsonify({"mensagem": "Funcionário atualizado com sucesso"}), 200

    except Error as err:
        print(f"Erro ao editar o funcionário: {err}")
        return jsonify({"erro": "Erro ao editar o funcionário"}), 500

    finally:
        cursor.close()
        conexao.close()


#ROTAS CLIENTES
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

#Rota para cadastrar cliente
@cliente_bp.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    #Rota para cadastrar um novo cliente
    dados = request.json
    resposta, status = ClienteController.cadastrar_cliente(dados)
    return jsonify(resposta), status

#Rota para listar clientes
@cliente_bp.route("/clientes", methods=["GET"])
def listar_clientes():
    #Rota para listar todos os clientes
    resposta, status = ClienteController.listar_clientes()
    return jsonify(resposta), status 

app.register_blueprint(cliente_bp)


#ROTA FORNECEDORES
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


#ROTAS COMBUSTIVEIS
#rota para cadastrar combustiveis
@combustivel_bp.route("/combustiveis", methods=["POST"])
def cadastrar_combustivel():
    #Rota para cadastrar um novo combustiveis
    dados = request.json
    resposta, status = CombustivelController.cadastrar_combustivel(dados)
    return jsonify(resposta), status

#rota para listar combustiveis
@combustivel_bp.route("/combustiveis", methods=["GET"])
def listar_combustiveis():
    #Rota para listar todos os combustíveis
    resposta, status = CombustivelController.listar_combustiveis()
    return jsonify(resposta), status   

app.register_blueprint(combustivel_bp)

#ROTA RESERVATORIOS
#rota para cadastrar reservatorios
@reservatorio_bp.route("/reservatorios", methods=["POST"])
def cadastrar_reservatorio():
    dados = request.json
    resposta, status = ReservatorioController.cadastrar_reservatorio(dados)
    return jsonify(resposta), status

#rota para listar reservatorios
@reservatorio_bp.route("/reservatorios", methods=["GET"])
def listar_reservatorios():
    resposta, status = ReservatorioController.listar_reservatorios()
    return jsonify(resposta), status

app.register_blueprint(reservatorio_bp)

#ROTAS ITEM
#rota para cadastrar itens
@item_bp.route("/item", methods=["POST"])
def cadastrar_item():
    #Rota para cadastrar um novo item
    dados = request.json
    resposta, status = ItemController.cadastrar_item(dados)
    return jsonify(resposta), status

#rota para listar itens
@item_bp.route("/item", methods=["GET"])
def listar_itens():
    #Rota para listar todos os itens
    resposta, status = ItemController.listar_itens()
    return jsonify(resposta), status   

#rota para remover item
@app.route('/delete-item/<codigo>', methods=['DELETE'])
def remover_item(codigo):
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        # Verifica se o item existe
        query_verificar = "SELECT CodigoBarras from item where CodigoBarras = %s"
        cursor.execute(query_verificar, (codigo,))
        if cursor.fetchone() is None:
            return jsonify({"erro": "Item não encontrado"}), 404

        # Remove o funcionário
        query_remover = "DELETE FROM item WHERE CodigoBarras = %s"
        cursor.execute(query_remover, (codigo,))
        conexao.commit()

        return jsonify({"mensagem": "Item removido com sucesso"}), 200

    except Error as err:
        print(f"Erro ao remover o Item: {err}")
        return jsonify({"erro": "Erro ao remover o Item"}), 500

    finally:
        cursor.close()
        conexao.close()

#Rota para buscar item
@app.route('/item/<CodigoBarras>', methods=['GET'])
def buscar_item(CodigoBarras):
    print(f"Buscando item com Código de Barras: {CodigoBarras}")  # Debug
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        query = """
            SELECT NomeItem, Categoria, QtdeEstoque, PrecUnitario, CodigoBarras from item where CodigoBarras = %s
        """
        cursor.execute(query, (CodigoBarras,))
        item = cursor.fetchone()

        if item is None:
            return jsonify({"erro": "Item não encontrado"}), 404

        item_data = {
            "NomeItem": item[0],
            "Categoria": item[1],
            "QtdeEstoque": item[2],
            "PrecUnitario": item[3],
            "CodigoBarras": item[4]
        }

        return jsonify(item_data), 200

    except Error as err:
        print(f"Erro ao buscar o item: {err}")
        return jsonify({"erro": "Erro ao buscar o item"}), 500

    finally:
        cursor.close()
        conexao.close()

#Rota para editar item
@app.route('/editar-item/<CodigoBarras>', methods=['PUT'])
def editar_item(CodigoBarras):
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()
    dados = request.json

    try:
        # Verifica se o item existe
        query_verificar = "SELECT CodigoBarras FROM item WHERE CodigoBarras = %s"
        cursor.execute(query_verificar, (CodigoBarras,))
        if cursor.fetchone() is None:
            return jsonify({"erro": "Item não encontrado"}), 404

        # Atualiza os dados do item
        query_atualizar = """
            UPDATE item
            SET Categoria = %s, NomeItem = %s, PrecUnitario = %s, QtdeEstoque = %s, funcionario_cpf = %s
            WHERE CodigoBarras = %s
        """
        cursor.execute(query_atualizar, (
            dados.get("Categoria"),
            dados.get("NomeItem"),
            dados.get("PrecUnitario"),
            dados.get("QtdeEstoque"),
            dados.get("funcionario_cpf"),
            CodigoBarras
        ))
        conexao.commit()

        return jsonify({"mensagem": "Item atualizado com sucesso"}), 200

    except Error as err:
        print(f"Erro ao editar o item: {err}")
        return jsonify({"erro": f"Erro ao editar o item: {err}"}), 500

    finally:
        cursor.close()
        conexao.close()


app.register_blueprint(item_bp)

#ROTAS PAGAMENTO
#rota para cadastrar pagamento
@pagamento_bp.route("/pagamento", methods=["POST"])
def cadastrar_pagamento():
    #Rota para cadastrar um novo pagamento
    dados = request.json
    resposta, status = PagamentoController.cadastrar_pagamento(dados)
    return jsonify(resposta), status

#rota para listar pagamentos
@pagamento_bp.route("/pagamento", methods=["GET"])
def listar_pagamentos():
    #Rota para listar todos os pagamentos
    resposta, status = PagamentoController.listar_pagamentos()
    return jsonify(resposta), status   

app.register_blueprint(pagamento_bp)


#ROTAS PARA VENDAS
#rota para cadastrar vendas
@app.route('/cadvenda', methods=['POST'])
def cadastrar_venda():
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()

    try:
        # Obtendo os dados do corpo da requisição
        dados = request.json

        cpf_cliente = dados.get("cpfCliente")
        cpf_funcionario = dados.get("cpfFuncionario")
        itens = dados.get("itens")
        valor = dados.get("valor")
        tipo_pagamento = dados.get("tipoPagamento")

        # Validação dos dados recebidos
        if not all([cpf_cliente, cpf_funcionario, itens, valor, tipo_pagamento]):
            return jsonify({"erro": "Dados incompletos"}), 400

        # Iniciar transação
        conexao.start_transaction()

        # Inserir venda na tabela registroVenda
        query_venda = """
            INSERT INTO registroVenda (cpfCliente, cpfFuncionario, itens, valor, tipoPagamento)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query_venda, (cpf_cliente, cpf_funcionario, itens, valor, tipo_pagamento))

        # Confirmar transação
        conexao.commit()

        return jsonify({"mensagem": "Venda cadastrada com sucesso!", "id": cursor.lastrowid}), 201

    except Error as err:
        conexao.rollback()  # Reverte mudanças em caso de erro
        print(f"Erro ao cadastrar venda: {err}")
        return jsonify({"erro": "Erro ao cadastrar venda"}), 500

    finally:
        cursor.close()
        conexao.close()

#rota para listar vendas
@app.route('/listarvendas', methods=['GET'])
def listar_vendas():
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor(dictionary=True)  # Retorna os resultados como dicionário

    try:
        # Consulta todas as vendas na tabela registroVenda
        query = "SELECT * FROM registroVenda"
        cursor.execute(query)
        vendas = cursor.fetchall()

        return jsonify(vendas), 200

    except Error as err:
        print(f"Erro ao listar vendas: {err}")
        return jsonify({"erro": "Erro ao listar vendas"}), 500

    finally:
        cursor.close()
        conexao.close()



#Rota login
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

if __name__ == '__main__':
    app.run(debug=True)