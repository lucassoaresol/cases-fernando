from itens.item import Item
from services.ibge import Ibge


class Ranking:
    def __init__(
        self, ibge: Ibge, nomes=[], localidades=[], sexo="", decadas=[]
    ) -> None:
        self.ibge = ibge
        self.is_nome = not nomes == None
        self.nomes = nomes
        self.is_localidade = not localidades == None
        self.localidades = localidades
        self.sexo = sexo
        self.is_decada = not decadas == None
        self.decadas = decadas
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

        if self.is_decada:
            if self.is_localidade:
                titulo += " e década"
            else:
                titulo += " por década"

        return f"{titulo}:\n"

    def adicionar_item(self, nome: str, frequencia=0, localidade="", decada=""):
        self.itens.append(
            Item(self.ibge, nome, frequencia, self.sexo, localidade, decada)
        )

    def ordernar_ranking(self):
        return self.itens.sort(key=lambda item: item.frequencia, reverse=True)

    def gera_ranking(self, localidade="", decada=""):
        if self.is_nome:
            for nome in self.nomes:
                self.adicionar_item(nome, localidade=localidade, decada=decada)

        else:
            dados = self.ibge.busca_ranking_geral(self.sexo, localidade, decada)
            if dados:
                for res in dados:
                    self.adicionar_item(
                        res["nome"], res["frequencia"], localidade, decada
                    )

        self.ordernar_ranking()

    def definir_ranking(self) -> str:
        conteudo = ""
        ranking = 1

        if self.itens:
            for item in self.itens:
                conteudo += f"{ranking}º - {item}\n"
                ranking += 1
        else:
            conteudo += "Nenhum ranking disponível"

        self.itens = []

        return conteudo

    def exibir_ranking(self) -> str:
        conteudo = self.definicao_titulo()

        if self.is_decada:
            for decada in self.decadas:
                conteudo += f"\nDécada: {decada}\n"
                if self.is_localidade:
                    for localidade in self.localidades:
                        conteudo += f"\nLocalidade: {localidade}\n"
                        self.gera_ranking(localidade, decada)
                        conteudo += self.definir_ranking()
                else:
                    self.gera_ranking(decada=decada)
                    conteudo += self.definir_ranking()

        elif self.is_localidade:
            for localidade in self.localidades:
                conteudo += f"\nLocalidade: {localidade}\n"
                self.gera_ranking(localidade)
                conteudo += self.definir_ranking()

        else:
            self.gera_ranking()
            conteudo += self.definir_ranking()

        return conteudo
