import redis
from services.ibge import Ibge


class Redis:
    def __init__(self, ibge: Ibge) -> None:
        self.ibge = ibge
        self.r = redis.Redis(host="localhost", port=6379, decode_responses=True)

    def key(self, base: str, sexo="", localidade="", decada="") -> str:
        if localidade:
            base += f"-{localidade}"

        if sexo:
            base += f"-{sexo}"

        if decada:
            base += f"-{decada}"

        return base

    def busca_ranking(
        self, nome: str = "", sexo: str = "", localidade: str = "", decada: str = ""
    ):
        return self.ibge.busca_ranking(nome, sexo, localidade, decada)

    def ranking(self, sexo="", localidade="", decada=""):
        name = self.key("ranking", sexo, localidade, decada)
        # resposta = self.r.json().get(name, "$")

        # if resposta:
        #     return resposta["res"]

        resposta = self.busca_ranking(sexo=sexo, localidade=localidade, decada=decada)

        if resposta:
            dados = resposta[0]["res"]
            self.r.json().set(
                name,
                "$",
                {
                    "res": dados,
                },
            )
            return dados
