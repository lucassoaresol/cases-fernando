from services.ibge import Ibge


class Item:
    def __init__(
        self,
        ibge: Ibge,
        nome: str,
        frequencia: int,
        sexo="",
        localidade="",
        decada="",
    ) -> None:
        self.ibge = ibge
        self.nome = nome.upper()
        self.sexo = sexo
        self.localidade = localidade
        self.decada = decada
        self.frequencia = frequencia if frequencia != 0 else self.busca_frequencia()

    def busca_frequencia(self) -> int:
        resposta = self.ibge.busca_ranking(
            self.nome, self.sexo, self.localidade, self.decada
        )
        frequencia = 0

        if resposta:
            dados = resposta[0]
            ind = -1
            if self.decada:
                ind = int((self.decada - 1930) / 10)
            frequencia = dados["res"][ind]["frequencia"]

        return frequencia

    def __str__(self) -> str:
        return f"{self.nome} - {self.frequencia}"
