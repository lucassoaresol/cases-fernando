from services.ibge import Ibge
from services.redis import Redis


class Item:
    def __init__(
        self,
        ibge: Ibge,
        nome: str,
        frequencia=0,
        sexo="",
        localidade="",
        decada="",
    ) -> None:
        self.redis = Redis(ibge)
        self.nome = nome.upper()
        self.sexo = self.define_sexo(sexo)
        self.localidade = localidade
        self.decada = self.define_decada(decada)
        self.frequencia = self.busca_frequencia(frequencia)

    def define_sexo(self, sexo=""):
        if sexo:
            sexo = sexo.upper()
            if sexo == "M" or sexo == "F":
                return sexo
            else:
                raise ValueError(
                    f"Sexo: {sexo} não é válido. \nDigite M (Masculino) ou F (Feminino)."
                )

    def define_decada(self, decada=0):
        if decada:
            if isinstance(decada, int):
                if decada < 1930 or decada > 2010 or decada % 10 != 0:
                    raise ValueError(f"Década: {decada} não é válida.")
                else:
                    return decada
            else:
                raise ValueError(f"Década: {decada} não é válida.")

    def busca_frequencia(self, frequencia: int) -> int:
        if frequencia == 0:
            resposta = self.redis.frequencia(
                self.nome, self.sexo, self.localidade, self.decada
            )

            if resposta:
                if self.decada == 1930:
                    return resposta[0]["frequencia"]

                for valor in resposta:
                    if self.decada:
                        if valor["periodo"].split("[")[1].endswith(str(self.decada)):
                            frequencia = valor["frequencia"]
                    else:
                        frequencia += valor["frequencia"]

        return frequencia

    def define_json(self):
        return {
            "nome": self.nome,
            "sexo": self.sexo,
            "localidade": self.localidade,
            "decada": self.decada,
            "frequencia": self.frequencia,
        }

    def __str__(self) -> str:
        return f"{self.nome} - {self.frequencia}"
