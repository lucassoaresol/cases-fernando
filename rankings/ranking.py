from itens.item import Item
from multiprocessing import cpu_count, Pool
from services.ibge import Ibge
import time
import json


def processar_combinacao(args):
    ibge, nome, sexo, localidade, decada = args
    itens = []

    if nome:
        item = Item(ibge, nome, sexo=sexo, localidade=localidade, decada=decada)
        itens.append(item)

    else:
        resposta = ibge.busca_ranking(sexo=sexo, localidade=localidade, decada=decada)

        if resposta:
            dados = resposta[0]["res"]
            for res in dados:
                item = Item(
                    ibge, res["nome"], res["frequencia"], sexo, localidade, decada
                )
                itens.append(item)

    return itens


class Ranking:
    def __init__(
        self, ibge: Ibge, nomes=[], sexo="", localidades=[], decadas=[], arquivo=""
    ) -> None:
        self.ibge = ibge
        self.nomes = nomes
        self.sexo = sexo
        self.localidades = localidades
        self.decadas = decadas
        self.arquivo = arquivo
        self.itens: list[Item] = []
        self.titulo = self.define_titulo()

    def define_titulo(self, titulo="Ranking geral dos nomes"):
        if self.nomes:
            titulo = "Ranking dos nomes"

        if self.sexo == "M":
            titulo += " do sexo Masculino"

        if self.sexo == "F":
            titulo += " do sexo Feminino"

        if self.localidades:
            titulo += f" por localidade"

        if self.decadas:
            if self.localidades:
                titulo += " e década"
            else:
                titulo += " por década"

        titulo += ":\n"

        return titulo

    def adiciona_item(self, item: Item):
        self.itens.append(item)

    def instancia_item(self, nome: str, frequencia=None, localidade="", decada=""):
        self.adiciona_item(
            Item(self.ibge, nome, frequencia, self.sexo, localidade, decada)
        )

    def orderna_ranking(self, ranking: list[Item]):
        return sorted(ranking, key=lambda item: item.frequencia, reverse=True)

    def busca_ranking(self):
        resposta = self.ibge.busca_ranking(sexo=self.sexo)

        if resposta:
            dados = resposta[0]["res"]
            for res in dados:
                self.instancia_item(res["nome"], res["frequencia"])

    def gera_combinacoes(self):
        combinacoes = []

        if self.arquivo:
            self.importa_json_nomes()

        if self.nomes:
            for nome in self.nomes:
                if self.localidades:
                    for localidade in self.localidades:
                        if self.decadas:
                            for decada in self.decadas:
                                combinacoes.append(
                                    (self.ibge, nome, self.sexo, localidade, decada)
                                )
                        else:
                            combinacoes.append(
                                (self.ibge, nome, self.sexo, localidade, None)
                            )

                elif self.decadas:
                    for decada in self.decadas:
                        combinacoes.append((self.ibge, nome, self.sexo, None, decada))

                else:
                    combinacoes.append((self.ibge, nome, self.sexo, None, None))

        elif self.localidades:
            for localidade in self.localidades:
                if self.decadas:
                    for decada in self.decadas:
                        combinacoes.append(
                            (self.ibge, None, self.sexo, localidade, decada)
                        )
                else:
                    combinacoes.append((self.ibge, None, self.sexo, localidade, None))

        elif self.decadas:
            for decada in self.decadas:
                combinacoes.append((self.ibge, None, self.sexo, None, decada))

        return combinacoes

    def gera_ranking(self):
        combinacoes = self.gera_combinacoes()

        if combinacoes:
            with Pool(cpu_count()) as executor:
                todos_itens = executor.map(processar_combinacao, combinacoes)
            for itens in todos_itens:
                for item in itens:
                    self.adiciona_item(item)
        else:
            self.busca_ranking()

    def monta_ranking(self, itens: list[Item]):
        ranking = ""

        if self.decadas:
            for decada in self.decadas:
                ranking += f"\nDécada: {decada}\n"
                if self.localidades:
                    for localidade in self.localidades:
                        ranking += f"\nLocalidade: {localidade}\n"
                        itens_ranking = [
                            item
                            for item in itens
                            if item.localidade == localidade and item.decada == decada
                        ]
                        ranking += self.define_ranking(itens_ranking)

                else:
                    itens_ranking = [item for item in itens if item.decada == decada]
                    ranking += self.define_ranking(itens_ranking)

        elif self.localidades:
            for localidade in self.localidades:
                ranking += f"\nLocalidade: {localidade}\n"
                itens_ranking = [
                    item for item in itens if item.localidade == localidade
                ]
                ranking += self.define_ranking(itens_ranking)

        else:
            ranking += self.define_ranking(itens)

        return ranking

    def define_ranking(self, itens: list[Item]):
        ranking = ""

        if itens:
            for index, item in enumerate(self.orderna_ranking(itens)):
                ranking += f"{index+1}º - {item}\n"

        else:
            ranking += "Nenhum ranking disponível"

        return ranking

    def mostra_ranking(self):
        ranking = self.monta_ranking(self.itens)
        print(self.titulo + ranking)

    def exporta_json_ranking(self):
        itens_json = [item.define_json() for item in self.orderna_ranking(self.itens)]
        nome_arquivo = f"saidas/{round(time.time() * 1000)}.json"

        with open(nome_arquivo, "w") as json_file:
            json.dump(itens_json, json_file, indent=2)

        return nome_arquivo

    def importa_json_nomes(self):
        nome_arquivo = f"{self.arquivo}.json"

        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)

        self.nomes = dados
