from Models.Combustivel import CombustivelModel
from flask import jsonify

class CombustivelController:
    @staticmethod
    def cadastrar_combustivel(dados):
        """Recebe os dados e chama o Model para cadastrar"""
        if not all(k in dados for k in ("nome", "preco_litro", "categoria", "quantidade_disponivel")):
            return {"erro": "Todos os campos são obrigatórios"}, 400

        sucesso = CombustivelModel.set_combustivel(
            dados["nome"],
            float(dados["preco_litro"]),
            dados["categoria"],
            float(dados["quantidade_disponivel"])
        )

        if sucesso:
            return {"mensagem": "Combustível cadastrado com sucesso!"}, 201
        else:
            return {"erro": "Erro ao cadastrar combustível"}, 500

    @staticmethod
    def listar_combustiveis():
        """Chama o Model para buscar todos os combustíveis"""
        combustiveis = CombustivelModel.get_combustivel()

        if combustiveis is not None:
            # Aqui você pode formatar a resposta conforme desejar
            return {"combustiveis": combustiveis}, 200
        else:
            return {"mensagem": "Nenhum combustível encontrado"}, 404