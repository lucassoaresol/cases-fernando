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
        self.titulo = self.define_titulo()

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

    def instancia_item(self, nome: str, frequencia=None, localidade="", decada=""):
        self.itens.append(
            Item(self.ibge, nome, frequencia, self.sexo, localidade, decada)
        )

    def orderna_ranking(self, ranking: list[Item]):
        return sorted(ranking, key=lambda item: item.frequencia, reverse=True)

    def busca_ranking(self, args=(None, None, None)):
        nome, localidade, decada = args
        localidade = self.define_localidade(localidade)
        decada = self.define_decada(decada)

        if nome:
            self.instancia_item(nome, localidade=localidade, decada=decada)

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

    def multi_ranking(self, combinacoes: list):
        if combinacoes:
            with ThreadPoolExecutor(cpu_count()) as executor:
                executor.map(self.busca_ranking, combinacoes)
        else:
            self.busca_ranking()

    def gera_ranking(self):
        combinacoes = []

        if self.arquivo:
            self.importa_json_nomes()

        if self.nomes:
            for nome in self.nomes:
                if self.localidades:
                    for localidade in self.localidades:
                        if self.decadas:
                            for decada in self.decadas:
                                combinacoes.append((nome, localidade, decada))
                        else:
                            combinacoes.append((nome, localidade, None))

                elif self.decadas:
                    for decada in self.decadas:
                        combinacoes.append((nome, None, decada))

                else:
                    combinacoes.append((nome, None, None))

        elif self.localidades:
            for localidade in self.localidades:
                if self.decadas:
                    for decada in self.decadas:
                        combinacoes.append((None, localidade, decada))
                else:
                    combinacoes.append((None, localidade, None))

        elif self.decadas:
            for decada in self.decadas:
                combinacoes.append((None, None, decada))

        self.multi_ranking(combinacoes)

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
        with ThreadPoolExecutor(cpu_count()) as executor:
            ranking = executor.submit(self.monta_ranking, self.itens)
            print(self.titulo + ranking.result())

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
