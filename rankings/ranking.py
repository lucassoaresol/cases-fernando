from itens import Item
from services import Ibge


class Ranking:
    def orderna_nomes(self, itens: list[Item]) -> list:
        nomes_ordem = sorted(itens, key=lambda item: item.frequencia, reverse=True)

        return [
            {"ranking": index + 1, "nome": item.nome}
            for index, item in enumerate(nomes_ordem)
        ]

    def monta_ranking(self, dados: list) -> str:
        result = ""

        for res in dados:
            ranking = res["ranking"]
            nome = res["nome"]

            result += f"{ranking}º - {nome}\n"

        return result

    def gera_ranking(self, nomes=[]) -> str:
        title = "Ranking dos nomes:"
        if nomes:
            itens = []

            for nome in nomes:
                item = Item(nome, Ibge().busca_frequencia(nome))
                itens.append(item)

            dados = self.orderna_nomes(itens)

        else:
            title = "Ranking geral dos nomes:"
            dados = Ibge().busca_ranking_geral()

        return f"{title}\n{self.monta_ranking(dados)}"
