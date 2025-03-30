from Models.Item import ItemModel
from flask import jsonify

class ItemController:
    @staticmethod
    @staticmethod
    def cadastrar_item(dados):
        """Recebe os dados e chama o Model para cadastrar um item."""
        try:
            if not all(k in dados for k in ("nome", "categoria", "quantidade_disponivel", "preco_unitario", "codigo_barras", "funcionario_cpf")):
                return {"erro": "Todos os campos são obrigatórios"}, 400

            print("Recebendo dados:", dados)  # Depuração

            sucesso = ItemModel.set_item(
                dados["nome"],
                dados["categoria"],
                int(dados["quantidade_disponivel"]),
                float(dados["preco_unitario"]),
                dados["codigo_barras"],
                dados["funcionario_cpf"]
            )

            if sucesso:
                return {"mensagem": "Item cadastrado com sucesso!"}, 201
            else:
                return {"erro": "Erro ao cadastrar item no banco de dados"}, 500
        
        except Exception as e:
            return {"erro": f"Exceção: {str(e)}"}, 500


    @staticmethod
    def listar_itens():
        """Chama o Model para buscar todos os itens"""
        itens = ItemModel.get_Item()

        if itens is not None:
            # Aqui você pode formatar a resposta conforme desejar
            return {"itens": itens}, 200
        else:
            return {"mensagem": "Nenhum item encontrado"}, 404