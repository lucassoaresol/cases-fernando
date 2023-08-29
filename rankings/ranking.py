from itens import Item
from statistics import mean


class Ranking:
    def orderna_nomes(self, itens: list[Item]) -> list | None:
        frequencias = [item.frequencia for item in itens]

        if mean(frequencias) != 0:
            nomes_ordem = sorted(itens, key=lambda item: item.frequencia, reverse=True)

            return [
                {"ranking": index + 1, "nome": item.nome}
                for index, item in enumerate(nomes_ordem)
            ]

    def gera_ranking(self, dados=[]) -> str:
        result = ""

        if dados:
            for res in dados:
                ranking = res["ranking"]
                nome = res["nome"]

                result += f"{ranking}º - {nome}\n"
        else:
            result = "Nenhum ranking disponível"

        return result
