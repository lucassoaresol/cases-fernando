import requests


class Ranking:
    def __init__(self, nomes_frequencia=[]) -> None:
        self.nomes_frequencia = nomes_frequencia

    def geral(self) -> dict:
        link = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking"
        resposta = requests.get(link).json()

        return resposta[0]["res"]

    def nomes(self):
        nomes_ordem = sorted(
            self.nomes_frequencia, key=lambda i: i["frequencia"], reverse=True
        )

        ranking = 1

        for nome in nomes_ordem:
            nome["ranking"] = ranking
            ranking += ranking

        return nomes_ordem
