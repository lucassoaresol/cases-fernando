import requests


class Item:
    def __init__(self, nomes: list[str]) -> None:
        self.nomes = nomes

    def obter_frequencia(self, nome: str) -> dict:
        link = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
        resposta = requests.get(link).json()
        frequencia = 0

        if resposta:
            frequencia = resposta[0]["res"][-1]["frequencia"]

        return {
            "nome": nome.upper(),
            "frequencia": frequencia,
        }

    def frequencia(self) -> list:
        return [self.obter_frequencia(nome) for nome in self.nomes]
