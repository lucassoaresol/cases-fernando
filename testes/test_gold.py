from contas.gold import ContaGold
import unittest


class TestContaGold(unittest.TestCase):
    def setUp(self):
        self.conta_gold = ContaGold("Fernando", 12345, 1000)

    def teste_conceder_emprestimo(self):
        self.assertEqual(
            self.conta_gold.conceder_emprestimo(500, 2),
            "Empréstimo de 500 concedido, a ser pago em 2 meses.",
        )

    def teste_aplicar_juros(self):
        self.conta_gold.conceder_emprestimo(500, 2)

        resultado = self.conta_gold.aplicar_juros()

        self.assertEqual(resultado, "Juros aplicados. Novo saldo do empréstimo: 510.0")

    def teste_aplicar_juros_none(self):
        resultado = self.conta_gold.aplicar_juros()

        self.assertEqual(resultado, "Não há empréstimo para aplicar juros.")


if __name__ == "__main__":
    unittest.main()
