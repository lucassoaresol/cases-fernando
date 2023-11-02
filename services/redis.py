import redis
from services.ibge import Ibge


class Redis:
    def __init__(self, ibge: Ibge) -> None:
        self.ibge = ibge
        self.r = redis.Redis(host="localhost", port=6379, decode_responses=True)

    def define_key(self, base: str, sexo="", localidade="", decada=""):
        if localidade:
            base += f"-{localidade}"

        if sexo:
            base += f"-{sexo}"

        if decada:
            base += f"-{decada}"

        return base

    def ranking(self, sexo="", localidade="", decada=""):
        name = self.define_key("ranking", sexo, localidade, decada)
        resposta = self.r.json().get(name, "$")

        if resposta:
            return resposta[0]

        resposta = self.ibge.busca_ranking(
            sexo=sexo, localidade=localidade, decada=decada
        )

        if resposta:
            dados = resposta[0]["res"]
            self.r.json().set(
                name,
                "$",
                dados,
            )
            return dados

    def frequencia(self, nome: str, sexo="", localidade="", decada=""):
        name = self.define_key(nome, sexo, localidade, decada)
        resposta = self.r.json().get(name, "$")

        if resposta:
            return resposta[0]

        resposta = self.ibge.busca_ranking(nome, sexo, localidade, decada)

        if resposta:
            dados = resposta[0]
            self.r.json().set(
                name,
                "$",
                dados["res"],
            )
            return dados["res"]

    def localidade(self, localidade: str):
        name = self.define_key("localidade", localidade=localidade)
        resposta = self.r.json().get(name, "$")

        if resposta:
            return resposta[0]

        resposta = self.ibge.busca_localidade(localidade)

        if resposta:
            self.r.json().set(
                name,
                "$",
                resposta,
            )
            return resposta
