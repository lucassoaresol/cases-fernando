from .api import Api


class Ibge:
    def __init__(self, api: Api, sexo="") -> None:
        self.api = api
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
        resposta = self.api.get(nome, self.params(localidade))
        frequencia = 0

        if resposta:
            frequencia = resposta[0]["res"][-1]["frequencia"]

        return frequencia

    def busca_ranking_geral(self, localidade="") -> list | None:
        resposta = self.api.get("ranking", self.params(localidade))

        if resposta:
            return resposta[0]["res"]
