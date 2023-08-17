from statistics import mean
from scripts import params, definicao_title
from services import Api


class Ranking:
    def __init__(self, api: Api, is_localidade: bool, is_decada: bool, sexo="") -> None:
        self.api = api
        self.is_localidade = is_localidade
        self.is_decada = is_decada
        self.sexo = sexo

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

    def ordem_nome(self, nomes_frequencia: list, localidade="", decada="") -> str:
        result = ""

        if localidade:
            frequencias = [nome_list["frequencia"] for nome_list in nomes_frequencia]

            result = f"\nLocalidade: {localidade}\n"

            if mean(frequencias) == 0:
                return result + "Nenhum ranking disponível"

        if decada:
            frequencias = [nome_list["frequencia"] for nome_list in nomes_frequencia]

            result = f"\nDécada: {decada}\n"

            if mean(frequencias) == 0:
                return result + "Nenhum ranking disponível"

        nomes_ordem = sorted(
            nomes_frequencia, key=lambda i: i["frequencia"], reverse=True
        )

        for index, nome_list in enumerate(nomes_ordem):
            nome = nome_list["nome"]
            ranking = index + 1

            result += f"{ranking}º - {nome}\n"

        return result

    def title(self, title: str) -> str:
        return definicao_title(title, self.is_localidade, self.is_decada, self.sexo)

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
        conteudo = self.title("Ranking geral dos nomes")

        if decadas:
            for elem in self.geral_decadas(decadas, localidades):
                result = f"\nDécada: {elem['decada']}\n" + elem["res"]
                conteudo += result
        elif localidades:
            conteudo += self.geral_localidades(localidades)
        else:
            conteudo += self.get()

        return conteudo

    def nomes_localidades(self, nomes: list, decada="") -> str:
        result = ""

        if decada:
            result = f"\nDécada: {decada}\n"

        for localidade_nomes in nomes:
            result += self.ordem_nome(
                localidade_nomes["res"], localidade_nomes["localidade"]
            )

        return result

    def nomes_decadas(self, nomes: list) -> str:
        result = ""

        for decada_nomes in nomes:
            if self.is_localidade:
                result += self.nomes_localidades(
                    decada_nomes["res"], decada_nomes["decada"]
                )
            else:
                result += self.ordem_nome(
                    decada_nomes["res"], decada=decada_nomes["decada"]
                )

        return result

    def nomes(self, nomes: list) -> str:
        conteudo = self.title("Ranking dos nomes")

        if self.is_decada:
            conteudo += self.nomes_decadas(nomes)

        elif self.is_localidade:
            conteudo += self.nomes_localidades(nomes)

        else:
            conteudo += self.ordem_nome(nomes)

        return conteudo
