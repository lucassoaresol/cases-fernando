from urllib3.util import Retry
from requests import Session
from requests.adapters import HTTPAdapter


class Api:
    def __init__(self, retry=3, timeout=5) -> None:
        self.retry = retry
        self.timeout = timeout

    prefix = "https://servicodados.ibge.gov.br/"

    base_url = f"{prefix}api/v2/censos/nomes"

    def get(self, endpoint: str, params: dict | None):
        sessao = Session()
        retries = Retry(total=self.retry, raise_on_redirect=True)
        sessao.mount(
            self.prefix,
            HTTPAdapter(max_retries=retries),
        )

        link = f"{self.base_url}/{endpoint}"
        return sessao.get(link, params=params, timeout=self.timeout).json()
