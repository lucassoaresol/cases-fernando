from itens.item import Item
from services.ibge import Ibge


class Ranking:
    def __init__(
        self, ibge: Ibge, nomes=[], sexo="", localidades=[], decadas=[]
    ) -> None:
        self.ibge = ibge
        self.nomes = nomes
        self.sexo = sexo
        self.localidades = localidades
        self.decadas = decadas
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

        if self.decadas:
            if self.localidades:
                self.titulo += " e década"
            else:
                self.titulo += " por década"

        self.titulo += ":\n"

    def adiciona_item(self, nome: str, frequencia=0, localidade="", decada=""):
        self.itens.append(
            Item(self.ibge, nome, frequencia, self.sexo, localidade, decada)
        )

    def orderna_ranking(self):
        return self.itens.sort(key=lambda item: item.frequencia, reverse=True)

    def busca_ranking(self, localidade="", decada=""):
        if self.nomes:
            for nome in self.nomes:
                self.adiciona_item(nome, localidade=localidade, decada=decada)

        else:
            resposta = self.ibge.busca_ranking(
                sexo=self.sexo, localidade=localidade, decada=decada
            )

            if resposta:
                dados = resposta[0]["res"]
                for res in dados:
                    self.adiciona_item(
                        res["nome"], res["frequencia"], localidade, decada
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
        if self.decadas:
            for decada in self.decadas:
                self.ranking += f"\nDécada: {decada}\n"
                if self.localidades:
                    for localidade in self.localidades:
                        self.ranking += f"\nLocalidade: {localidade}\n"
                        self.busca_ranking(localidade, decada)
                        self.define_ranking()
                else:
                    self.busca_ranking(decada=decada)
                    self.define_ranking()

        elif self.localidades:
            for localidade in self.localidades:
                self.ranking += f"\nLocalidade: {localidade}\n"
                self.busca_ranking(localidade)
                self.define_ranking()

        else:
            self.busca_ranking()
            self.define_ranking()

    def mostra_ranking(self):
        print(self.titulo + self.ranking)
