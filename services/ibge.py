import requests


class Ibge:
    def busca_frequencia(self, nome: str) -> int:
        link = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
        resposta = requests.get(link).json()
        frequencia = 0

        if resposta:
            frequencia = resposta[0]["res"][-1]["frequencia"]

        return frequencia

    def busca_ranking_geral(self) -> list:
        link = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking"

        resposta = requests.get(link).json()

        return resposta[0]["res"]
