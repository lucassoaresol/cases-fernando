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

    def params(self, sexo="", localidade="") -> dict | None:
        payload = {}

        if localidade:
            payload["localidade"] = localidade

        if sexo:
            payload["sexo"] = sexo

        if payload:
            return payload

    def busca_frequencia(self, nome: str, sexo="", localidade="") -> int:
        link = f"{self.base_url}/{nome}"
        resposta = self.sessao.get(
            link, params=self.params(sexo, localidade), timeout=self.timeout
        ).json()
        frequencia = 0

        if resposta:
            frequencia = resposta[0]["res"][-1]["frequencia"]

        return frequencia

    def busca_ranking_geral(self, sexo="", localidade="") -> list | None:
        link = f"{self.base_url}/ranking"
        resposta = self.sessao.get(
            link, params=self.params(sexo, localidade), timeout=self.timeout
        ).json()

        if resposta:
            return resposta[0]["res"]
