from statistics import mean


class Ranking:
    def orderna_nomes(self, nomes_frequencia: list) -> list | None:
        frequencias = [nome_list["frequencia"] for nome_list in nomes_frequencia]

        if mean(frequencias) != 0:
            nomes_ordem = sorted(
                nomes_frequencia, key=lambda i: i["frequencia"], reverse=True
            )

            return [
                {"ranking": index + 1, "nome": nome_list["nome"]}
                for index, nome_list in enumerate(nomes_ordem)
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
