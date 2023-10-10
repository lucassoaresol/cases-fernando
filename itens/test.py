from itens.item import Item
from services.ibge import Ibge
from unittest.mock import Mock
import unittest


class TestItem(unittest.TestCase):
    def setUp(self):
        self.nome = "João"
        self.frequencia = 5000
        self.localidade = "Br"
        self.sexo = "M"
        self.decada = 1990
        self.ibge_mock = Mock(Ibge)
        self.ibge_mock.busca_localidade.return_value = {
            "id": 31,
            "sigla": "MG",
            "nome": "Minas Gerais",
            "regiao": {"id": 3, "sigla": "SE", "nome": "Sudeste"},
        }
        self.ibge_mock.busca_ranking.return_value = [
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

    def teste_criar_item_com_valores_validos(self):
        item = Item(self.ibge_mock, self.nome, self.frequencia)
        self.assertEqual(item.nome, self.nome.upper())
        self.assertEqual(item.frequencia, self.frequencia)

    def teste_criar_item_com_sexo_invalido(self):
        item = Item(self.ibge_mock, self.nome, sexo="bk")
        self.assertEqual(item.sexo, None)

    def teste_criar_item_com_decada(self):
        item = Item(self.ibge_mock, self.nome, 0, self.sexo, self.localidade, 1990)
        self.assertEqual(item.decada, 1990)

    def teste_criar_item_sem_frequencia(self):
        item = Item(self.ibge_mock, self.nome)
        self.assertEqual(item.frequencia, 794118)

    def teste_criar_item_sem_frequencia_com_decada(self):
        item = Item(self.ibge_mock, self.nome, decada=self.decada)
        self.assertEqual(item.frequencia, 273960)


if __name__ == "__main__":
    unittest.main()
