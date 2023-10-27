from scripts.decada import define_decada
from scripts.localidade import define_localidade
from scripts.sexo import define_sexo
from services.ibge import Ibge


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
        self.ibge = ibge
        self.nome = nome.upper()
        self.sexo = define_sexo(sexo)
        self.localidade = define_localidade(ibge, localidade)
        self.decada = define_decada(decada)
        self.frequencia = self.busca_frequencia(frequencia)

    def busca_frequencia(self, frequencia: int) -> int:
        if frequencia == 0:
            resposta = self.ibge.busca_ranking(
                self.nome, self.sexo, self.localidade, self.decada
            )

            if resposta:
                dados = resposta[0]

                if self.decada == 1930:
                    return dados["res"][0]["frequencia"]

                for valor in dados["res"]:
                    if self.decada:
                        if valor["periodo"].split("[")[1].endswith(str(self.decada)):
                            frequencia = valor["frequencia"]
                    else:
                        frequencia += valor["frequencia"]

        return frequencia

    def __str__(self) -> str:
        return f"{self.nome} - {self.frequencia}"
