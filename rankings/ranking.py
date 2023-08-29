from itens import Item
from statistics import mean


class Ranking:
    def gera_ranking_geral(self, dados=[]) -> str:
        result = ""

        if dados:
            for res in dados:
                ranking = res["ranking"]
                nome = res["nome"]

                result += f"{ranking}º - {nome}\n"
        else:
            result = "Nenhum ranking disponível"

        return result

    def gera_ranking_nomes(self, itens: list[Item]) -> str:
        frequencias = [item.frequencia for item in itens]

        if mean(frequencias) == 0:
            return "Nenhum ranking disponível"

        nomes_ordem = sorted(itens, key=lambda item: item.frequencia, reverse=True)
        result = ""
        ranking = 1

        for item in nomes_ordem:
            result += f"{ranking}º - {item.nome}\n"
            ranking += 1

        return result
