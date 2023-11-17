from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.exceptions import MaxRetryError
from urllib3.util import Retry
from services.redis import Redis


class Ibge:
    def __init__(self, retry=3, timeout=5) -> None:
        self.retry = retry
        self.timeout = timeout
        self.base_url = "https://servicodados.ibge.gov.br/api/"
        self.cache = Redis()

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

    def busca_cache(self, cache_key):
        return self.cache.busca(cache_key)

    def busca_ranking(self, nome="", sexo="", localidade="", decada=""):
        url = f"{self.base_url}v2/censos/nomes/"

        if nome:
            url += nome
        else:
            url += "ranking"

        if self.cache.verificar_conexao():
            cache_key = f"{nome}:{localidade}:{sexo}:{decada}"
            resposta = self.busca_cache(cache_key)
            if resposta:
                return resposta
            else:
                resposta = self.busca(url, self.params(sexo, localidade, decada))
                self.cache.define(cache_key, resposta)
                return resposta
        else:
            return self.busca(url, self.params(sexo, localidade, decada))

    def busca_localidade(self, localidade):
        if isinstance(localidade, str):
            localidade = localidade.upper()

        url = f"{self.base_url}v1/localidades/estados/{localidade}"

        return self.busca(url)
