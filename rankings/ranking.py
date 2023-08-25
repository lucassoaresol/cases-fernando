class Ranking:
    def orderna_nomes(self, nomes_frequencia: list) -> list:
        nomes_ordem = sorted(
            nomes_frequencia, key=lambda i: i["frequencia"], reverse=True
        )

        return [
            {"ranking": index + 1, "nome": nome_list["nome"]}
            for index, nome_list in enumerate(nomes_ordem)
        ]

    def gera_ranking(self, dados: list) -> str:
        result = ""

        for res in dados:
            ranking = res["ranking"]
            nome = res["nome"]

            result += f"{ranking}º - {nome}\n"

        return result
