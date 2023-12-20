from contas.silver import ContaSilver
import unittest


class TestContaSilver(unittest.TestCase):
    def setUp(self):
        self.conta_silver = ContaSilver("Fernando", 12345, 1000)

    def teste_realizar_emprestimo(self):
        self.assertEqual(
            self.conta_silver.conceder_emprestimo(500, 5),
            "Empréstimo não disponível para Conta Básica.",
        )


if __name__ == "__main__":
    unittest.main()
