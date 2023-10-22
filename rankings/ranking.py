from itens.item import Item
from scripts.decada import define_decada
from scripts.localidade import define_localidade
from scripts.sexo import define_sexo
from services.ibge import Ibge


class Ranking:
    def __init__(
        self, ibge: Ibge, nomes=[], sexo="", localidades=[], decadas=[]
    ) -> None:
        self.ibge = ibge
        self.nomes = nomes
        self.sexo = define_sexo(sexo)
        self.localidades = localidades
        self.decadas = decadas
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

    def instancia_item(self, nome: str, frequencia=0, localidade="", decada="") -> Item:
        return Item(self.ibge, nome, frequencia, self.sexo, localidade, decada)

    def orderna_ranking(self, ranking: list[Item]) -> list[Item]:
        return sorted(ranking, key=lambda item: item.frequencia, reverse=True)

    def busca_ranking(self, localidade="", decada="") -> list[Item]:
        localidade = define_localidade(self.ibge, localidade)
        decada = define_decada(decada)
        itens = []

        if self.nomes:
            for nome in self.nomes:
                itens.append(
                    self.instancia_item(nome, localidade=localidade, decada=decada)
                )

        else:
            resposta = self.ibge.busca_ranking(
                sexo=self.sexo, localidade=localidade, decada=decada
            )

            if resposta:
                dados = resposta[0]["res"]
                for res in dados:
                    self.instancia_item(
                        res["nome"], res["frequencia"], localidade, decada
                    )

        return itens

    def define_ranking(self, itens: list[Item]):
        ranking = 1

        if itens:
            for item in itens:
                self.ranking += f"{ranking}º - {item}\n"
                ranking += 1
        else:
            self.ranking += "Nenhum ranking disponível"

    def gera_ranking(self):
        if self.decadas:
            for decada in self.decadas:
                self.ranking += f"\nDécada: {decada}\n"
                if self.localidades:
                    for localidade in self.localidades:
                        self.ranking += f"\nLocalidade: {localidade}\n"
                        self.define_ranking(self.busca_ranking(localidade, decada))
                else:
                    self.define_ranking(self.busca_ranking(decada=decada))

        elif self.localidades:
            for localidade in self.localidades:
                self.ranking += f"\nLocalidade: {localidade}\n"
                self.define_ranking(self.busca_ranking(localidade))

        else:
            self.define_ranking(self.busca_ranking())

    def mostra_ranking(self):
        print(self.titulo + self.ranking)
