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
        self.frequencia = frequencia if frequencia != 0 else self.busca_frequencia()

    def busca_frequencia(self) -> int:
        resposta = self.ibge.busca_ranking(
            self.nome, self.sexo, self.localidade, self.decada
        )

        if resposta:
            dados = resposta[0]
            if self.decada:
                ind = int((self.decada - 1930) / 10)
                frequencia = dados["res"][ind]["frequencia"]
            else:
                frequencia = 0
                for valor in dados["res"]:
                    frequencia += valor["frequencia"]

        return frequencia

    def __str__(self) -> str:
        return f"{self.nome} - {self.frequencia}"
