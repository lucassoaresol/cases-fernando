from itens.item import Item
from services.ibge import Ibge


class Ranking:
    def __init__(self, ibge: Ibge, nomes=[], localidades=[], sexo="") -> None:
        self.ibge = ibge
        self.is_nome = not nomes == None
        self.nomes = nomes
        self.is_localidade = not localidades == None
        self.localidades = localidades
        self.sexo = sexo
        self.itens: list[Item] = []

    def definicao_titulo(self) -> str:
        titulo = "Ranking geral dos nomes"

        if self.is_nome:
            titulo = "Ranking dos nomes"

        if self.sexo == "M":
            titulo += " do sexo Masculino"

        if self.sexo == "F":
            titulo += " do sexo Feminino"

        if self.is_localidade:
            titulo += f" por localidade"

        return f"{titulo}:\n"

    def adicionar_item(self, nome: str, frequencia=0, localidade=""):
        self.itens.append(Item(self.ibge, nome, frequencia, self.sexo, localidade))

    def ordernar_ranking(self):
        return self.itens.sort(key=lambda item: item.frequencia, reverse=True)

    def gera_ranking(self, localidade=""):
        if self.is_nome:
            for nome in self.nomes:
                self.adicionar_item(nome, localidade=localidade)

        else:
            dados = self.ibge.busca_ranking_geral(self.sexo, localidade)
            if dados:
                for res in dados:
                    self.adicionar_item(res["nome"], res["frequencia"], localidade)

        self.ordernar_ranking()

    def exibir_ranking(self) -> str:
        conteudo = self.definicao_titulo()

        if self.is_localidade:
            for localidade in self.localidades:
                conteudo += f"\nLocalidade: {localidade}\n"
                self.gera_ranking(localidade)
                ranking = 1

                if self.itens:
                    for item in self.itens:
                        conteudo += f"{ranking}º - {item}\n"
                        ranking += 1
                else:
                    conteudo += "Nenhum ranking disponível"

                self.itens = []

            return conteudo

        self.gera_ranking()
        ranking = 1

        for item in self.itens:
            conteudo += f"{ranking}º - {item}\n"
            ranking += 1

        return conteudo
