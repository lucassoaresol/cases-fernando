from statistics import mean
from scripts import params, definicao_title
from services import Api


class Ranking:
    def __init__(
        self, api: Api, nomes_frequencia=[], nomes_frequencia_localidade=[]
    ) -> None:
        self.api = api
        self.nomes_frequencia = nomes_frequencia
        self.nomes_frequencia_localidade = nomes_frequencia_localidade

    def get(self, localidade="", sexo="") -> str:
        result = ""

        if localidade:
            result = f"\nLocalidade: {localidade}\n"

        resposta = self.api.get("ranking", params=params(localidade, sexo))

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

    def geral(self, localidades=[], sexo="") -> str:
        if localidades:
            conteudo = ""
            for index, localidade in enumerate(localidades):
                if index == 0:
                    conteudo = definicao_title(
                        "Ranking geral dos nomes", localidade, sexo
                    )

                conteudo += self.get(localidade, sexo)
            return conteudo

        return definicao_title("Ranking geral dos nomes", sexo=sexo) + self.get(
            sexo=sexo
        )

    def nomes(self, sexo="") -> str:
        if self.nomes_frequencia_localidade:
            conteudo = ""
            for index, localidade_nomes in enumerate(self.nomes_frequencia_localidade):
                localidade = localidade_nomes["localidade"]
                self.nomes_frequencia = localidade_nomes["res"]

                if index == 0:
                    conteudo = definicao_title("Ranking dos nomes", localidade, sexo)

                conteudo += self.ordem_nome(localidade)

            return conteudo

        return definicao_title("Ranking dos nomes", sexo=sexo) + self.ordem_nome()
