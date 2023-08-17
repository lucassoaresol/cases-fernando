from scripts import params
from services import Api


class Item:
    def __init__(self, api: Api, nomes: list[str], sexo="") -> None:
        self.api = api
        self.nomes = nomes
        self.sexo = sexo

    def get_frequencia(self, nome: str, localidade="", decada="") -> dict:
        resposta = self.api.get(nome, params(localidade, self.sexo, decada))
        frequencia = 0

        if resposta:
            frequencia = resposta[0]["res"][-1]["frequencia"]

        return {
            "nome": nome.upper(),
            "frequencia": frequencia,
        }

    def frequencia_nome(self, localidade="", decada="") -> list:
        return [self.get_frequencia(nome, localidade, decada) for nome in self.nomes]

    def frequencia_localidades(self, localidades: list, decada="") -> list:
        return [
            {
                "localidade": localidade,
                "res": self.frequencia_nome(localidade, decada),
            }
            for localidade in localidades
        ]

    def frequencia_decadas(self, decadas: list, localidades=[]) -> list:
        if localidades:
            return [
                {
                    "decada": decada,
                    "res": self.frequencia_localidades(localidades, decada),
                }
                for decada in decadas
            ]
        return [
            {
                "decada": decada,
                "res": self.frequencia_nome(decada=decada),
            }
            for decada in decadas
        ]

    def frequencia(self, localidades=[], decadas=[]) -> list:
        if decadas:
            return self.frequencia_decadas(decadas, localidades)
        elif localidades:
            return self.frequencia_localidades(localidades)
        else:
            return self.frequencia_nome()
