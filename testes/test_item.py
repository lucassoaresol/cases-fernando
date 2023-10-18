from itens.item import Item
from testes.mock import TestMock
import unittest


class TestItem(unittest.TestCase):
    def setUp(self):
        self.mock = TestMock()

    def teste_criar_item_com_valores_validos(self):
        item = Item(self.mock.ibge, self.mock.nome, self.mock.frequencia)
        self.assertEqual(item.nome, self.mock.nome.upper())
        self.assertEqual(item.frequencia, self.mock.frequencia)

    def teste_criar_item_com_sexo_invalido(self):
        item = Item(self.mock.ibge, self.mock.nome, sexo="bk")
        self.assertEqual(item.sexo, None)

    def teste_criar_item_com_decada(self):
        item = Item(
            self.mock.ibge,
            self.mock.nome,
            0,
            self.mock.sexo,
            self.mock.localidade,
            self.mock.decada,
        )
        self.assertEqual(item.decada, self.mock.decada)

    def teste_criar_item_sem_frequencia(self):
        item = Item(self.mock.ibge, self.mock.nome)
        self.assertEqual(item.frequencia, 794118)

    def teste_criar_item_sem_frequencia_com_decada(self):
        item = Item(self.mock.ibge, self.mock.nome, decada=self.mock.decada)
        self.assertEqual(item.frequencia, 273960)


if __name__ == "__main__":
    unittest.main()
