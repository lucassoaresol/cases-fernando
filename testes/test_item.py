from itens.item import Item
from services.ibge import Ibge
from testes import constantes
from unittest.mock import Mock
import unittest


class TestItem(unittest.TestCase):
    def setUp(self):
        ibge = Mock(Ibge)
        ibge.busca_localidade.return_value = constantes.siglas_estados
        ibge.busca_ranking.return_value = constantes.nome_sem_parametros
        self.ibge = ibge

    def teste_criar_item_com_valores_validos(self):
        item = Item(self.ibge, "FERNANDO", 61551, "M", "RS", 1930)
        self.assertEqual(item.nome, "FERNANDO")
        self.assertEqual(item.frequencia, 61551)

    def teste_criar_item_com_sexo_invalido(self):
        with self.assertRaises(ValueError):
            Item(self.ibge, "FERNANDO", sexo="bk")

    def teste_criar_item_sem_localidade(self):
        item = Item(self.ibge, "FERNANDO")
        self.assertEqual(item.define_localidade(), "BR")

    def teste_criar_item_com_localidade(self):
        item = Item(self.ibge, "FERNANDO", localidade="RS")
        self.assertEqual(item.define_localidade("RS"), 43)

    def teste_criar_item_com_localidade_invalida(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.nome_sem_parametros
        ibge.busca_localidade.return_value = None
        item = Item(ibge, "FERNANDO", localidade="bk")
        with self.assertRaises(ValueError):
            item.define_localidade("bk")

    def teste_criar_item_com_decada(self):
        item = Item(self.ibge, "FERNANDO", decada=2010)
        self.assertEqual(item.frequencia, 61551)

    def teste_criar_item_com_decada_invalida(self):
        with self.assertRaises(ValueError):
            Item(self.ibge, "FERNANDO", decada=1900)

    def teste_criar_item_com_decada_invalida_texto(self):
        with self.assertRaises(ValueError):
            Item(self.ibge, "FERNANDO", decada="rsrs")

    def teste_criar_item_sem_frequencia(self):
        item = Item(self.ibge, "FERNANDO")
        self.assertEqual(item.frequencia, 556346)

    def teste_criar_item_sem_frequencia_com_decada(self):
        item = Item(self.ibge, "FERNANDO", decada=1930)
        self.assertEqual(item.frequencia, 2204)

    def teste_item_define_json(self):
        item = Item(self.ibge, "FERNANDO", sexo="M", localidade="RS", decada=1930)
        self.assertDictEqual(
            item.define_json(),
            {
                "nome": "FERNANDO",
                "sexo": "M",
                "localidade": "RS",
                "decada": 1930,
                "frequencia": 2204,
            },
        )


if __name__ == "__main__":
    unittest.main()
