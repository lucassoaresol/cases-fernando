import requests
from scripts import params


class Item:
    def __init__(self, nomes: list[str], sexo="") -> None:
        self.nomes = nomes
        self.sexo = sexo

    def get_frequencia(self, nome: str, localidade="") -> dict:
        link = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
        resposta = requests.get(link, params=params(localidade, self.sexo)).json()
        frequencia = 0

        if resposta:
            frequencia = resposta[0]["res"][-1]["frequencia"]

        return {
            "nome": nome.upper(),
            "frequencia": frequencia,
        }

    def frequencia_nome(self, localidade="") -> list:
        return [self.get_frequencia(nome, localidade) for nome in self.nomes]

    def frequencia(self, localidades=[]) -> list:
        if localidades:
            return [
                {"localidade": localidade, "res": self.frequencia_nome(localidade)}
                for localidade in localidades
            ]
        return self.frequencia_nome()
