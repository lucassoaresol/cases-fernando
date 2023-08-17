import requests


class Ranking:
    def geral(self) -> str:
        link = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking"
        result = ""

        resposta = requests.get(link).json()

        for res in resposta[0]["res"]:
            ranking = res["ranking"]
            nome = res["nome"]

            result += f"{ranking}º - {nome}\n"

        return result

    def nomes(self, nomes_frequencia: list) -> str:
        result = ""

        nomes_ordem = sorted(
            nomes_frequencia, key=lambda i: i["frequencia"], reverse=True
        )

        for index, nome_list in enumerate(nomes_ordem):
            nome = nome_list["nome"]
            ranking = index + 1

            result += f"{ranking}º - {nome}\n"

        return result
