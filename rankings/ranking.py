from itens import Item
from services import Ibge


class Ranking:
    def monta_ranking_geral(self, dados: list) -> str:
        result = "Ranking geral dos nomes:\n"

        for res in dados:
            ranking = res["ranking"]
            nome = res["nome"]

            result += f"{ranking}º - {nome}\n"

        return result

    def monta_ranking_nomes(self, itens: list[Item]) -> str:
        nomes_ordem = sorted(itens, key=lambda item: item.frequencia, reverse=True)
        result = "Ranking dos nomes:\n"
        ranking = 1

        for item in nomes_ordem:
            result += f"{ranking}º - {item.nome}\n"
            ranking += 1

        return result

    def gera_ranking(self, nomes=[]) -> str:
        if nomes:
            itens = []

            for nome in nomes:
                item = Item(nome, Ibge().busca_frequencia(nome))
                itens.append(item)

            return self.monta_ranking_nomes(itens)

        else:
            return self.monta_ranking_geral(Ibge().busca_ranking_geral())
