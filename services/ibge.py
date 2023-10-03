from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.exceptions import MaxRetryError
from urllib3.util import Retry


class Ibge:
    def __init__(self, retry: int, timeout: int) -> None:
        retries = Retry(total=retry, raise_on_redirect=True)
        self.timeout = timeout
        self.base_url = "https://servicodados.ibge.gov.br/api/"
        self.sessao = Session()
        self.sessao.mount("https://", HTTPAdapter(max_retries=retries))

    def params(self, sexo="", localidade="") -> dict | None:
        payload = {}

        if localidade:
            payload["localidade"] = localidade

        if sexo:
            payload["sexo"] = sexo

        if payload:
            return payload

    def busca_ranking(self, nome="", sexo="", localidade=""):
        link = f"{self.base_url}v2/censos/nomes/"

        if nome:
            link += nome
        else:
            link += "ranking"

        try:
            return self.sessao.get(
                link,
                params=self.params(sexo, localidade),
                timeout=self.timeout,
            ).json()
        except MaxRetryError:
            print("Número de tentativas excedido")
