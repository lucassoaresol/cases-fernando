from itens.item import Item
from services.ibge import Ibge


class Ranking:
    def __init__(self, ibge: Ibge) -> None:
        self.ibge = ibge
        self.itens: list[Item] = []
        self.titulo = "Ranking geral dos nomes"
        self.ranking = ""

    def define_titulo(self, nomes=[], sexo="", localidades=[]):
        if nomes:
            self.titulo = "Ranking dos nomes"

        if sexo == "M":
            self.titulo += " do sexo Masculino"

        if sexo == "F":
            self.titulo += " do sexo Feminino"

        if localidades:
            self.titulo += f" por localidade"

        self.titulo += ":\n"

    def adiciona_item(self, nome: str, frequencia: int):
        self.itens.append(Item(nome, frequencia))

    def orderna_ranking(self):
        return self.itens.sort(key=lambda item: item.frequencia, reverse=True)

    def busca_ranking(self, nomes=[], sexo="", localidade=""):
        if nomes:
            for nome in nomes:
                resposta = self.ibge.busca_ranking(nome, sexo, localidade)
                frequencia = 0

                if resposta:
                    dados = resposta[0]
                    frequencia = dados["res"][-1]["frequencia"]

                self.adiciona_item(nome, frequencia)

        else:
            resposta = self.ibge.busca_ranking(
                sexo=sexo,
                localidade=localidade,
            )

            if resposta:
                dados = resposta[0]["res"]
                for res in dados:
                    self.adiciona_item(res["nome"], res["frequencia"])

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

    def gera_ranking(self, nomes=[], sexo="", localidades=[]):
        if localidades:
            for localidade in localidades:
                self.ranking += f"\nLocalidade: {localidade}\n"
                self.busca_ranking(nomes, sexo, localidade)
                self.define_ranking()

        else:
            self.busca_ranking(nomes, sexo)
            self.define_ranking()

    def mostra_ranking(self):
        print(self.titulo + self.ranking)
