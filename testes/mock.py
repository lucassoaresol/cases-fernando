from services.ibge import Ibge
from unittest.mock import Mock


class TestMock:
    def __init__(self) -> None:
        self.nome = "João"
        self.frequencia = 5000
        self.localidade = "Br"
        self.sexo = "M"
        self.decada = 1990
        self.ibge = Mock(Ibge)
        self.ibge.busca_localidade.return_value = {
            "id": 31,
            "sigla": "MG",
            "nome": "Minas Gerais",
            "regiao": {"id": 3, "sigla": "SE", "nome": "Sudeste"},
        }
        self.ibge.busca_ranking.return_value = [
            {
                "nome": "JOAO",
                "sexo": None,
                "localidade": "BR",
                "res": [
                    {"periodo": "1930[", "frequencia": 60155},
                    {"periodo": "[1930,1940[", "frequencia": 141772},
                    {"periodo": "[1940,1950[", "frequencia": 256001},
                    {"periodo": "[1950,1960[", "frequencia": 396438},
                    {"periodo": "[1960,1970[", "frequencia": 429148},
                    {"periodo": "[1970,1980[", "frequencia": 279975},
                    {"periodo": "[1980,1990[", "frequencia": 273960},
                    {"periodo": "[1990,2000[", "frequencia": 352552},
                    {"periodo": "[2000,2010[", "frequencia": 794118},
                ],
            }
        ]
