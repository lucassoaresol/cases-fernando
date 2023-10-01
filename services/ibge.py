from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class Ibge:
    def __init__(self, retry: int, timeout: int) -> None:
        prefix = "https://servicodados.ibge.gov.br/"
        retries = Retry(total=retry, raise_on_redirect=True)
        self.timeout = timeout
        self.base_url = f"{prefix}api/v2/censos/nomes"
        self.sessao = Session()
        self.sessao.mount(
            prefix,
            HTTPAdapter(max_retries=retries),
        )

    def params(self, sexo="", localidade="", decada="") -> dict | None:
        payload = {}

        if localidade:
            payload["localidade"] = localidade

        if sexo:
            payload["sexo"] = sexo

        if decada:
            payload["decada"] = decada

        if payload:
            return payload

    def busca_frequencia(self, nome: str, sexo="", localidade="", decada="") -> int:
        link = f"{self.base_url}/{nome}"
        resposta = self.sessao.get(
            link, params=self.params(sexo, localidade, decada), timeout=self.timeout
        ).json()
        frequencia = 0

        if resposta:
            ind = -1
            if decada:
                ind = int((decada - 1930) / 10)

            frequencia = resposta[0]["res"][ind]["frequencia"]

        return frequencia

    def busca_ranking_geral(self, sexo="", localidade="", decada="") -> list | None:
        link = f"{self.base_url}/ranking"
        resposta = self.sessao.get(
            link, params=self.params(sexo, localidade, decada), timeout=self.timeout
        ).json()

        if resposta:
            return resposta[0]["res"]
