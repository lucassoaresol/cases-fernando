from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.exceptions import MaxRetryError
from urllib3.util import Retry


class Ibge:
    def __init__(self, retry=3, timeout=5) -> None:
        self.retry = retry
        self.timeout = timeout
        self.base_url = "https://servicodados.ibge.gov.br/api/"

    def config_sessao(self):
        retries = Retry(total=self.retry, raise_on_redirect=True)
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

    def busca(self, url, params=None):
        self.config_sessao()
        try:
            return self.sessao.get(
                url,
                params=params,
                timeout=self.timeout,
            ).json()
        except MaxRetryError:
            print("Número de tentativas excedido")

    def busca_ranking(self, nome="", sexo="", localidade="", decada=""):
        url = f"{self.base_url}v2/censos/nomes/"

        if nome:
            url += nome
        else:
            url += "ranking"

        return self.busca(url, self.params(sexo, localidade, decada))

    def busca_localidade(self, localidade):
        if isinstance(localidade, str):
            localidade = localidade.upper()

        url = f"{self.base_url}v1/localidades/estados/{localidade}"

        return self.busca(url)
