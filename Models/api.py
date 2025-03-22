from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

DB_NOME = "mydb"
DB_USUARIO = "root"
DB_SENHA = "Rafael@2003"
DB_HOST = "localhost"
DB_PORT = "3306"

def abrirConexao():
    try:
        conn = mysql.connector.connect(
            database=DB_NOME,
            user=DB_USUARIO,
            password=DB_SENHA,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Banco de dados conectado com sucesso.")
        return conn
    except Exception as error:
        print(f"Erro ao conectar com Banco de Dados: {error}")
        return None


# CRUD para tabela de venda
@app.route('/venda', methods=['POST'])
def criar_venda():
    data = request.json
    conn = abrirConexao()
    if conn is None:
        return jsonify({'message': 'Erro ao conectar com o banco de dados.'}), 500
    cur = conn.cursor()
    try:
        cur.execute(""" 
        INSERT INTO venda (id_venda, data_hora, Venda_combustivel_tipo_combustivel, Pagamento_id_pagamento, cliente_cpf, funcionario_cpf) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (data['id_venda'], data['data_hora'], data['Venda_combustivel_tipo_combustivel'], data['Pagamento_id_pagamento'], data['cliente_cpf'], data['funcionario_cpf']))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({'message': 'Erro ao criar venda.', 'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

    return jsonify({'id': data['id_venda']}), 201

@app.route('/venda', methods=['GET'])
def leitura_venda():
    conn = abrirConexao()
    if conn is None:
        return jsonify({'message': 'Erro ao conectar com o banco de dados.'}), 500
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM venda;')
        vendas = cur.fetchall()
    except Exception as e:
        return jsonify({'message': 'Erro ao obter vendas.', 'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

    return jsonify(vendas)

@app.route('/venda/<int:id>', methods=['PUT'])
def atualizar_venda(id):
    data = request.json
    conn = abrirConexao()
    if conn is None:
        return jsonify({'message': 'Erro ao conectar com o banco de dados.'}), 500
    cur = conn.cursor()
    try:
        cur.execute(""" 
        UPDATE venda SET data_hora = %s, Venda_combustivel_tipo_combustivel = %s, Pagamento_id_pagamento = %s, cliente_cpf = %s, funcionario_cpf = %s 
        WHERE id_venda = %s
        """, (data['data_hora'], data['Venda_combustivel_tipo_combustivel'], data['Pagamento_id_pagamento'], data['cliente_cpf'], data['funcionario_cpf'], id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({'message': 'Erro ao atualizar venda.', 'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

    return jsonify({'message': 'Venda atualizada com sucesso.'})

@app.route('/venda/<int:id>', methods=['DELETE'])
def deletar_venda(id):
    conn = abrirConexao()
    if conn is None:
        return jsonify({'message': 'Erro ao conectar com o banco de dados.'}), 500
    cur = conn.cursor()
    try:
        cur.execute('DELETE FROM venda WHERE id_venda = %s;', (id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({'message': 'Erro ao deletar venda.', 'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

    return jsonify({'message': 'Venda deletada com sucesso.'})

# CRUD para tabela de solicitacao_remessa
@app.route('/solicitacao_remessa', methods=['POST'])
def criar_solicitacao_remessa():
    data = request.json
    conn = abrirConexao()
    if conn is None:
        return jsonify({'message': 'Erro ao conectar com o banco de dados.'}), 500
    cur = conn.cursor()
    try:
        cur.execute(""" 
        INSERT INTO solicitacao_remessa (idsolicitacaoRemessa, DataSolicitacao, DataEntrega, Status, fornecedor_cnpj, funcionario_cpf) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (data['idsolicitacaoRemessa'], data['DataSolicitacao'], data['DataEntrega'], data['Status'], data['fornecedor_cnpj'], data['funcionario_cpf']))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({'message': 'Erro ao criar solicitação de remessa.', 'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

    return jsonify({'id': data['idsolicitacaoRemessa']}), 201

@app.route('/solicitacao_remessa', methods=['GET'])
def leitura_solicitacao_remessa():
    conn = abrirConexao()
    if conn is None:
        return jsonify({'message': 'Erro ao conectar com o banco de dados.'}), 500
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM solicitacao_remessa;')
        solicitacoes = cur.fetchall()
    except Exception as e:
        return jsonify({'message': 'Erro ao obter solicitações de remessa.', 'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

    return jsonify(solicitacoes)

@app.route('/solicitacao_remessa/<int:id>', methods=['PUT'])
def atualizar_solicitacao_remessa(id):
    data = request.json
    conn = abrirConexao()
    if conn is None:
        return jsonify({'message': 'Erro ao conectar com o banco de dados.'}), 500
    cur = conn.cursor()
    try:
        cur.execute(""" 
        UPDATE solicitacao_remessa SET DataSolicitacao = %s, DataEntrega = %s, Status = %s, fornecedor_cnpj = %s, funcionario_cpf = %s 
        WHERE idsolicitacaoRemessa = %s
        """, (data['DataSolicitacao'], data['DataEntrega'], data['Status'], data['fornecedor_cnpj'], data['funcionario_cpf'], id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({'message': 'Erro ao atualizar solicitação de remessa.', 'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

    return jsonify({'message': 'Solicitação de remessa atualizada com sucesso.'})

@app.route('/solicitacao_remessa/<int:id>', methods=['DELETE'])
def deletar_solicitacao_remessa(id):
    conn = abrirConexao()
    if conn is None:
        return jsonify({'message': 'Erro ao conectar com o banco de dados.'}), 500
    cur = conn.cursor()
    try:
        cur.execute('DELETE FROM solicitacao_remessa WHERE idsolicitacaoRemessa = %s;', (id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({'message': 'Erro ao deletar solicitação de remessa.', 'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

    return jsonify({'message': 'Solicitação de remessa deletada com sucesso.'})