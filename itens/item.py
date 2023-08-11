import requests


class Item:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def get_frequencia(self) -> dict:
        link = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{self.nome}"
        resposta = requests.get(link).json()

        return {
            "nome": self.nome,
            "frequencia": resposta[0]["res"][-1]["frequencia"],
        }
