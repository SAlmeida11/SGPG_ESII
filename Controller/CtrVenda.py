from Models.Venda import VendaModel
from flask import jsonify
from datetime import datetime

class VendaController:
    @staticmethod
    def cadastrar_venda(dados):
        """Recebe os dados e chama o Model para cadastrar uma venda"""
        try:
            if not all(k in dados for k in ("data_hora", "Venda_combustivel_idvendaCombustivel", "Pagamento_id_pagamento", "cliente_cpf", "funcionario_cpf")):
                return {"erro": "Todos os campos são obrigatórios"}, 400

            print("Recebendo dados:", dados)  # Depuração

            sucesso = VendaModel.set_venda(
                dados["data_hora"],
                dados["Venda_combustivel_idvendaCombustivel"],
                dados["Pagamento_id_pagamento"],
                dados["cliente_cpf"],
                dados["funcionario_cpf"]
            )

            if sucesso:
                return {"mensagem": "Venda cadastrada com sucesso!"}, 201
            else:
                return {"erro": "Erro ao cadastrar venda no banco de dados"}, 500
        
        except Exception as e:
            return {"erro": f"Exceção: {str(e)}"}, 500

    @staticmethod
    def listar_vendas():
        """Chama o Model para buscar todas as vendas"""
        vendas = VendaModel.get_vendas()

        if vendas is not None:
            # Aqui você pode formatar a resposta conforme desejar
            return {"vendas": vendas}, 200
        else:
            return {"mensagem": "Nenhuma venda encontrada"}, 404
