from itens.item import Item
from services.ibge import Ibge


class Ranking:
    def __init__(self, ibge: Ibge, nomes=[], sexo="", localidades=[]) -> None:
        self.ibge = ibge
        self.nomes = nomes
        self.sexo = sexo
        self.localidades = localidades
        self.itens: list[Item] = []
        self.titulo = "Ranking geral dos nomes"
        self.ranking = ""

    def define_titulo(self):
        if self.nomes:
            self.titulo = "Ranking dos nomes"

        if self.sexo == "M":
            self.titulo += " do sexo Masculino"

        if self.sexo == "F":
            self.titulo += " do sexo Feminino"

        if self.localidades:
            self.titulo += f" por localidade"

        self.titulo += ":\n"

    def adiciona_item(self, nome: str, frequencia=0, localidade=""):
        self.itens.append(
            Item(
                self.ibge,
                nome,
                frequencia,
                self.sexo,
                localidade,
            )
        )

    def orderna_ranking(self):
        return self.itens.sort(key=lambda item: item.frequencia, reverse=True)

    def busca_ranking(self, localidade=""):
        if self.nomes:
            for nome in self.nomes:
                self.adiciona_item(nome, localidade=localidade)

        else:
            resposta = self.ibge.busca_ranking(
                sexo=self.sexo,
                localidade=localidade,
            )

            if resposta:
                dados = resposta[0]["res"]
                for res in dados:
                    self.adiciona_item(
                        res["nome"],
                        res["frequencia"],
                        localidade,
                    )

        self.orderna_ranking()

    def define_ranking(self):
        ranking = 1

        if self.itens:
            for item in self.itens:
                self.ranking += f"{ranking}º - {item}\n"
                ranking += 1
        else:
            self.ranking += "Nenhum ranking disponível"

        self.itens = []

    def gera_ranking(self):
        if self.localidades:
            for localidade in self.localidades:
                self.ranking += f"\nLocalidade: {localidade}\n"
                self.busca_ranking(localidade)
                self.define_ranking()

        else:
            self.busca_ranking()
            self.define_ranking()

    def mostra_ranking(self):
        print(self.titulo + self.ranking)
