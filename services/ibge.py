from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.exceptions import MaxRetryError
from urllib3.util import Retry


class Ibge:
    def __init__(self, retry=3, timeout=5) -> None:
        retries = Retry(total=retry, raise_on_redirect=True)
        self.timeout = timeout
        self.base_url = "https://servicodados.ibge.gov.br/api/"
        self.sessao = Session()
        self.sessao.mount("https://", HTTPAdapter(max_retries=retries))

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

    def busca_ranking(self, nome="", sexo="", localidade="", decada=""):
        link = f"{self.base_url}v2/censos/nomes/"

        if nome:
            link += nome
        else:
            link += "ranking"

        try:
            return self.sessao.get(
                link,
                params=self.params(sexo, localidade, decada),
                timeout=self.timeout,
            ).json()
        except MaxRetryError:
            print("Número de tentativas excedido")

    def busca_localidade(self, localidade):
        if isinstance(localidade, str):
            localidade = localidade.upper()

        link = f"{self.base_url}v1/localidades/estados/{localidade}"

        try:
            return self.sessao.get(
                link,
                timeout=self.timeout,
            ).json()
        except MaxRetryError:
            print("Número de tentativas excedido")
