from statistics import mean
from scripts import params, definicao_title
from services import Api


class Ranking:
    def __init__(
        self, api: Api, sexo="", nomes_frequencia=[], nomes_frequencia_localidade=[]
    ) -> None:
        self.api = api
        self.sexo = sexo
        self.nomes_frequencia = nomes_frequencia
        self.nomes_frequencia_localidade = nomes_frequencia_localidade

    def get(self, localidade="", decada="") -> str:
        result = ""

        if localidade:
            result = f"\nLocalidade: {localidade}\n"

        resposta = self.api.get("ranking", params=params(localidade, self.sexo, decada))

        if resposta:
            for res in resposta[0]["res"]:
                ranking = res["ranking"]
                nome = res["nome"]
                result += f"{ranking}º - {nome}\n"

            return result

        return result + "Nenhum ranking disponível"

    def ordem_nome(self, localidade="") -> str:
        result = ""

        if localidade:
            frequencias = [
                nome_list["frequencia"] for nome_list in self.nomes_frequencia
            ]

            result = f"\nLocalidade: {localidade}\n"

            if mean(frequencias) == 0:
                return result + "Nenhum ranking disponível"

        nomes_ordem = sorted(
            self.nomes_frequencia, key=lambda i: i["frequencia"], reverse=True
        )

        for index, nome_list in enumerate(nomes_ordem):
            nome = nome_list["nome"]
            ranking = index + 1

            result += f"{ranking}º - {nome}\n"

        return result

    def geral_localidades(self, localidades: list, decada="") -> str:
        conteudo = ""

        for localidade in localidades:
            conteudo += self.get(localidade, decada)

        return conteudo

    def geral_decadas(self, decadas: list, localidades=[]) -> list:
        if localidades:
            return [
                {"decada": decada, "res": self.geral_localidades(localidades, decada)}
                for decada in decadas
            ]
        return [
            {"decada": decada, "res": self.get(decada=decada)} for decada in decadas
        ]

    def geral(self, localidades=[], decadas=[]) -> str:
        is_localidade = not localidades == None
        is_decada = not decadas == None

        conteudo = definicao_title(
            "Ranking geral dos nomes", is_localidade, is_decada, self.sexo
        )

        if decadas:
            for elem in self.geral_decadas(decadas, localidades):
                result = f"\nDécada: {elem['decada']}\n"
                result += elem["res"]
                conteudo += result
        elif localidades:
            conteudo += self.geral_localidades(localidades)
        else:
            conteudo += self.get()

        return conteudo

    def nomes(self, sexo="", decadas=[]) -> str:
        is_localidade = not len(self.nomes_frequencia_localidade) == 0
        is_decada = not decadas == None

        conteudo = definicao_title("Ranking dos nomes", is_localidade, is_decada, sexo)

        if self.nomes_frequencia_localidade:
            for localidade_nomes in self.nomes_frequencia_localidade:
                localidade = localidade_nomes["localidade"]
                self.nomes_frequencia = localidade_nomes["res"]
                conteudo += self.ordem_nome(localidade)

        else:
            conteudo += self.ordem_nome()

        return conteudo
