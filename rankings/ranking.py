from itens.item import Item
from scripts.decada import define_decada
from scripts.localidade import define_localidade
from scripts.sexo import define_sexo
from services.ibge import Ibge
import time
import json


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
        self.ranking_json = []

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

    def adiciona_item(
        self, itens: list, resposta=None, nome="", localidade="", decada=""
    ):
        if resposta:
            dados = resposta[0]["res"]
            for res in dados:
                itens.append(
                    self.instancia_item(
                        res["nome"], res["frequencia"], localidade, decada
                    )
                )
        else:
            itens.append(
                self.instancia_item(nome, localidade=localidade, decada=decada)
            )

    def orderna_ranking(self, ranking: list[Item]) -> list[Item]:
        return sorted(ranking, key=lambda item: item.frequencia, reverse=True)

    def busca_ranking(self, localidade="", decada="") -> list[Item]:
        localidade = define_localidade(self.ibge, localidade)
        decada = define_decada(decada)
        itens = []

        if self.nomes:
            for nome in self.nomes:
                self.adiciona_item(
                    itens, nome=nome, localidade=localidade, decada=decada
                )

        else:
            resposta = self.ibge.busca_ranking(
                sexo=self.sexo, localidade=localidade, decada=decada
            )

            self.adiciona_item(itens, resposta, localidade=localidade, decada=decada)

        return itens

    def define_ranking(self, itens: list[Item]):
        ranking = 1
        ranking_itens = []

        if itens:
            for item in itens:
                ranking_itens.append(
                    {
                        "nome": item.nome,
                        "frequencia": item.frequencia,
                        "ranking": ranking,
                    }
                )
                self.ranking += f"{ranking}º - {item}\n"
                ranking += 1
        else:
            self.ranking += "Nenhum ranking disponível"

        return ranking_itens

    def gera_ranking(self):
        if self.decadas:
            for decada in self.decadas:
                self.ranking += f"\nDécada: {decada}\n"
                if self.localidades:
                    for localidade in self.localidades:
                        self.ranking += f"\nLocalidade: {localidade}\n"
                        ranking = self.busca_ranking(localidade, decada)
                        self.ranking_json.append(
                            {
                                "localidade": localidade,
                                "sexo": self.sexo,
                                "decada": decada,
                                "res": self.define_ranking(
                                    self.orderna_ranking(ranking)
                                ),
                            }
                        )

                else:
                    ranking = self.busca_ranking(decada=decada)
                    self.ranking_json.append(
                        {
                            "localidade": "BR",
                            "sexo": self.sexo,
                            "decada": decada,
                            "res": self.define_ranking(self.orderna_ranking(ranking)),
                        }
                    )

        elif self.localidades:
            for localidade in self.localidades:
                self.ranking += f"\nLocalidade: {localidade}\n"
                ranking = self.busca_ranking(localidade)
                self.ranking_json.append(
                    {
                        "localidade": localidade,
                        "sexo": self.sexo,
                        "res": self.define_ranking(self.orderna_ranking(ranking)),
                    }
                )

        else:
            ranking = self.busca_ranking()
            self.ranking_json.append(
                {
                    "localidade": "BR",
                    "sexo": self.sexo,
                    "res": self.define_ranking(self.orderna_ranking(ranking)),
                }
            )

    def mostra_ranking(self):
        print(self.titulo + self.ranking)

    def exporta_json_ranking(self):
        with open(f"saidas/{round(time.time() * 1000)}.json", "w") as json_file:
            json.dump(self.ranking_json, json_file, indent=2)
