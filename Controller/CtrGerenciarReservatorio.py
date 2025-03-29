from Models.ReservatorioCombustivel import ReservatorioModel
from flask import jsonify

class ReservatorioController:
    @staticmethod
    def cadastrar_reservatorio(dados):
        """Recebe os dados e chama o Model para cadastrar um reservatório"""
        # Verifica se todos os campos obrigatórios foram enviados.
        # O front-end envia "capacidade", "nivelAtual", "temperatura" e "tipoCombustivel" (que é o ID do combustível)
        if not all(k in dados for k in ("capacidade", "nivelAtual", "temperatura", "tipoCombustivel")):
            return {"erro": "Todos os campos são obrigatórios"}, 400

        sucesso = ReservatorioModel.set_reservatorio(
            float(dados["capacidade"]),
            float(dados["nivelAtual"]),  # Mapeia 'nivelAtual' para a coluna 'nivel'
            float(dados["temperatura"]),
            dados["tipoCombustivel"]      # Este valor deve ser o ID do combustível selecionado
        )

        if sucesso:
            return {"mensagem": "Reservatório cadastrado com sucesso!"}, 201
        else:
            return {"erro": "Erro ao cadastrar reservatório"}, 500

    @staticmethod
    def listar_reservatorios():
        """Chama o Model para buscar todos os reservatórios"""
        reservatorios = ReservatorioModel.get_reservatorio()

        if reservatorios is not None:
            return {"reservatorios": reservatorios}, 200
        else:
            return {"mensagem": "Nenhum reservatório encontrado"}, 404
