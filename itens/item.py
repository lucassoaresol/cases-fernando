from scripts import params
from services import Api


class Item:
    def __init__(self, api: Api, nomes: list[str], sexo="") -> None:
        self.api = api
        self.nomes = nomes
        self.sexo = sexo

    def get_frequencia(self, nome: str, localidade="") -> dict:
        resposta = self.api.get(nome, params(localidade, self.sexo))
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
