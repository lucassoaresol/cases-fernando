import requests
from scripts import params


class Ibge:
    def __init__(self, sexo="") -> None:
        self.sexo = sexo

    def busca_frequencia(self, nome: str, localidade="") -> int:
        link = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
        resposta = requests.get(link, params=params(localidade, self.sexo)).json()
        frequencia = 0

        if resposta:
            frequencia = resposta[0]["res"][-1]["frequencia"]

        return frequencia

    def busca_ranking_geral(self, localidade="") -> list | None:
        link = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking"

        resposta = requests.get(link, params=params(localidade, self.sexo)).json()

        if resposta:
            return resposta[0]["res"]
