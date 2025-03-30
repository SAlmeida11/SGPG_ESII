from Models.Pagamento import PagamentoModel
from flask import jsonify

class PagamentoController:
    @staticmethod
    @staticmethod
    def cadastrar_pagamento(dados):
        """Recebe os dados e chama o Model para cadastrar um pagamento. Valor, FormaPagamento, Parcelado, Desconto, Juros, IntituiicaoCartaoCred_cnpj"""
        try:
            if not all(k in dados for k in ("Valor", "FormaPagamento", "Parcelado", "Desconto", "Juros", "IntituiicaoCartaoCred_cnpj")):
                return {"erro": "Todos os campos são obrigatórios"}, 400

            print("Recebendo dados:", dados)  # Depuração

            sucesso = PagamentoModel.set_pagamento(
                float(dados["Valor"]),
                dados["FormaPagamento"],
                int(dados["Parcelado"]),
                float(dados["Desconto"]),
                float(dados["Juros"]),
                dados["IntituiicaoCartaoCred_cnpj"]
            )

            if sucesso:
                return {"mensagem": "pagamento cadastrado com sucesso!"}, 201
            else:
                return {"erro": "Erro ao cadastrar pagamento no banco de dados"}, 500
        
        except Exception as e:
            return {"erro": f"Exceção: {str(e)}"}, 500


    @staticmethod
    def listar_pagamentos():
        """Chama o Model para buscar todos os pagamentos"""
        pagamentos = PagamentoModel.get_pagamento()

        if pagamentos is not None:
            # Aqui você pode formatar a resposta conforme desejar
            return {"pagamento": pagamentos}, 200
        else:
            return {"mensagem": "Nenhum pagamento encontrado"}, 404