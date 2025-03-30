from Models.Cliente import ClienteModel
from flask import jsonify
from datetime import datetime

def formatar_data(data):
    try:
        # Converter a string de timestamp para o formato esperado pelo banco de dados
        data_obj = datetime.strptime(data, '%a, %d %b %Y %H:%M:%S %Z')  # Formato do timestamp
        return data_obj.strftime('%Y-%m-%d')  # Formato compatível com o banco
    except ValueError:
        raise ValueError("Formato de data inválido.")

class ClienteController:
    @staticmethod
    def cadastrar_cliente(dados):
        """Recebe os dados e chama o Model para cadastrar"""
        campos_necessarios = (
        "logradouro", "numero", "bairro", "cidade", "estado", "cep",
        "cpf", "nome", "tipo", "dataCadastro"
        )
        if not all(k in dados for k in campos_necessarios):
            return {"erro": "Todos os campos são obrigatórios"}, 400
        
        sucesso = ClienteModel.set_cliente(
            dados["logradouro"],
            int(dados["numero"]),
            dados["bairro"],
            dados["cidade"],
            dados["estado"],
            dados["cep"],
            dados["cpf"],
            dados["nomeCliente"],
            dados["tipo"],
            formatar_data(dados["dataCadastro"])
        )

        if sucesso:
            return {"mensagem": "Cliente cadastrado com sucesso!"}, 201
        else:
            return {"erro": "Erro ao cadastrar cliente"}, 500

    @staticmethod
    def listar_clientes():
        """Chama o Model para buscar todos os clientes"""
        clientes = ClienteModel.get_cliente()

        if clientes is not None:
            # Aqui você pode formatar a resposta conforme desejar
            return {"clientes": clientes}, 200
        else:
            return {"mensagem": "Nenhum cliente encontrado"}, 404