import requests


class Ibge:
    def __init__(self, sexo="") -> None:
        self.sexo = sexo

    def params(self, localidade="") -> dict | None:
        payload = {}

        if localidade:
            payload["localidade"] = localidade

        if self.sexo:
            payload["sexo"] = self.sexo

        if payload:
            return payload

    def busca_frequencia(self, nome: str, localidade="") -> int:
        link = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
        resposta = requests.get(link, params=self.params(localidade)).json()
        frequencia = 0

        if resposta:
            frequencia = resposta[0]["res"][-1]["frequencia"]

        return frequencia

    def busca_ranking_geral(self, localidade="") -> list | None:
        link = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking"

        resposta = requests.get(link, params=self.params(localidade)).json()

        if resposta:
            return resposta[0]["res"]
