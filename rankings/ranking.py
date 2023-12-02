from concurrent.futures import ThreadPoolExecutor
from itens.item import Item
from multiprocessing import cpu_count
from services.ibge import Ibge
import time
import json


class Ranking:
    def __init__(
        self, ibge: Ibge, nomes=[], sexo="", localidades=[], decadas=[], arquivo=""
    ) -> None:
        self.ibge = ibge
        self.nomes = nomes
        self.sexo = self.define_sexo(sexo)
        self.localidades = localidades
        self.decadas = decadas
        self.arquivo = arquivo
        self.itens: list[Item] = []
        self.titulo = "Ranking geral dos nomes"
        self.ranking = ""

    def define_sexo(self, sexo=""):
        if sexo:
            sexo = sexo.upper()
            if sexo == "M" or sexo == "F":
                return sexo
            else:
                raise ValueError(
                    f"Sexo: {sexo} não é válido. \nDigite M (Masculino) ou F (Feminino)."
                )

    def define_localidade(self, localidade=""):
        if not localidade or localidade == "BR":
            return "BR"

        resposta = self.ibge.busca_localidade(localidade)

        if resposta:
            return resposta["id"]
        else:
            raise ValueError(f"Localidade: {localidade} não é válida.")

    def define_decada(self, decada=0):
        if decada:
            if isinstance(decada, int):
                if decada < 1930 or decada > 2010 or decada % 10 != 0:
                    raise ValueError(f"Década: {decada} não é válida.")
                else:
                    return decada
            else:
                raise ValueError(f"Década: {decada} não é válida.")

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

    def instancia_item(self, nome: str, frequencia=None):
        item = Item(
            self.ibge, nome, frequencia, self.sexo, self.localidade, self.decada
        )
        self.itens.append(item)
        return item

    def orderna_ranking(self, ranking: list[Item]):
        return sorted(ranking, key=lambda item: item.frequencia, reverse=True)

    def busca_ranking(self, localidade="", decada=""):
        self.localidade = self.define_localidade(localidade)
        self.decada = self.define_decada(decada)
        itens_ranking = []

        if self.arquivo:
            self.importa_json_nomes()

        if self.nomes:
            with ThreadPoolExecutor(cpu_count()) as executor:
                itens_ranking = executor.map(self.instancia_item, self.nomes)

        else:
            resposta = self.ibge.busca_ranking(
                sexo=self.sexo, localidade=self.localidade, decada=self.decada
            )

            if resposta:
                dados = resposta[0]["res"]
                for res in dados:
                    itens_ranking.append(
                        self.instancia_item(
                            res["nome"],
                            res["frequencia"],
                        )
                    )

        return itens_ranking

    def define_ranking(self, itens: list[Item]):
        if itens:
            for index, item in enumerate(self.orderna_ranking(itens)):
                self.ranking += f"{index+1}º - {item}\n"

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

        return self.ranking

    def mostra_ranking(self, ranking: str):
        self.define_titulo()
        print(self.titulo + ranking)

    def exporta_json_ranking(self):
        itens_json = [item.define_json() for item in self.itens]
        nome_arquivo = f"saidas/{round(time.time() * 1000)}.json"

        with open(nome_arquivo, "w") as json_file:
            json.dump(itens_json, json_file, indent=2)

        return nome_arquivo

    def importa_json_nomes(self):
        nome_arquivo = f"{self.arquivo}.json"

        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)

        self.nomes = dados
