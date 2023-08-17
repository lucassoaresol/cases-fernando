from statistics import mean
from scripts import params, definicao_title
from services import Api


class Ranking:
    def __init__(self, api: Api, is_localidade: bool, sexo="") -> None:
        self.api = api
        self.is_localidade = is_localidade
        self.sexo = sexo

    def get(self, localidade="") -> str:
        result = ""

        if localidade:
            result = f"\nLocalidade: {localidade}\n"

        resposta = self.api.get("ranking", params=params(localidade, self.sexo))

        if resposta:
            for res in resposta[0]["res"]:
                ranking = res["ranking"]
                nome = res["nome"]
                result += f"{ranking}º - {nome}\n"

            return result

        return result + "Nenhum ranking disponível"

    def ordem_nome(self, nomes_frequencia: list, localidade="") -> str:
        result = ""

        if localidade:
            frequencias = [nome_list["frequencia"] for nome_list in nomes_frequencia]

            result = f"\nLocalidade: {localidade}\n"

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
        return definicao_title(title, self.is_localidade, self.sexo)

    def geral(self, localidades=[]) -> str:
        conteudo = self.title("Ranking geral dos nomes")

        if localidades:
            for localidade in localidades:
                conteudo += self.get(localidade)
        else:
            conteudo += self.get()

        return conteudo

    def nomes(self, nomes: list) -> str:
        conteudo = self.title("Ranking dos nomes")

        if self.is_localidade:
            for localidade_nomes in nomes:
                conteudo += self.ordem_nome(
                    localidade_nomes["res"], localidade_nomes["localidade"]
                )
        else:
            conteudo += self.ordem_nome(nomes)

        return conteudo
