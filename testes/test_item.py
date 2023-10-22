from itens.item import Item
from testes import constantes
import unittest


class TestItem(unittest.TestCase):
    def teste_criar_item_com_valores_validos(self):
        item = Item(constantes.ibge, "FERNANDO", 61551, "M", "RS", 1930)
        self.assertEqual(item.nome, "FERNANDO")
        self.assertEqual(item.frequencia, 61551)

    def teste_criar_item_com_sexo_invalido(self):
        with self.assertRaises(ValueError):
            Item(constantes.ibge, "FERNANDO", sexo="bk")

    def teste_criar_item_com_decada_invalida(self):
        with self.assertRaises(ValueError):
            Item(constantes.ibge, "FERNANDO", decada=1900)

    def teste_criar_item_com_decada_invalida_texto(self):
        with self.assertRaises(ValueError):
            Item(constantes.ibge, "FERNANDO", decada="rsrs")

    def teste_criar_item_sem_frequencia(self):
        item = Item(constantes.ibge, "FERNANDO")
        self.assertEqual(item.frequencia, 61551)

    def teste_criar_item_sem_frequencia_com_decada(self):
        item = Item(constantes.ibge, "FERNANDO", decada=1930)
        self.assertEqual(item.frequencia, 2204)


if __name__ == "__main__":
    unittest.main()
