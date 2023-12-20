from contas.factory import FactoryContas
from contas.gold import ContaGold
from contas.silver import ContaSilver
import unittest


class TestFactory(unittest.TestCase):
    def setUp(self):
        self.factory = FactoryContas()
        self.conta_silver = ContaSilver("Fernando", 1, 1000)
        self.conta_gold = ContaGold("Pedro", 2, 5000, 0.02)
        self.factory.contas = {
            "Fernando": self.conta_silver,
            "Pedro": self.conta_gold,
        }

    def teste_criar_conta_silver(self):
        resposta = self.factory.criar_conta("Lucas", 100)
        self.assertIn("Conta Silver criada com sucesso", resposta)

    def teste_criar_conta_gold(self):
        resposta = self.factory.criar_conta("Maria", 10000)
        self.assertIn("Conta Gold criada com sucesso", resposta)

    def teste_obter_conta_existente(self):
        self.factory.criar_conta("Maria", 10000)
        conta = self.factory.obter_conta("Maria")
        self.assertIsInstance(conta, ContaGold)

    def teste_obter_conta_inexistente(self):
        conta = self.factory.obter_conta("Eva")
        self.assertIsNone(conta)

    def teste_depositar_em_conta(self):
        resposta = self.factory.depositar_em_conta(self.conta_silver, 500)
        self.assertEqual(resposta, "Depósito realizado com sucesso.")

    def teste_sacar_da_conta(self):
        resposta = self.factory.sacar_da_conta(self.conta_gold, 500)
        self.assertEqual(resposta, "Saque realizado com sucesso.")

    def teste_realizar_emprestimo_conta_gold(self):
        resposta = self.factory.realizar_emprestimo(self.conta_gold, 1000, 12)
        self.assertIn("Empréstimo de 1000 concedido", resposta)

    def teste_realizar_emprestimo_conta_gold_erro(self):
        resposta = self.factory.realizar_emprestimo(self.conta_silver, 1000, 12)
        self.assertEqual(
            "Empréstimo não disponível para este tipo de conta.",
            resposta,
        )

    def teste_aplicar_juros_conta_gold_falha(self):
        resposta = self.factory.aplicar_juros_conta_gold(self.conta_silver)
        self.assertEqual(resposta, "Juros aplicáveis somente para contas Gold.")

    def teste_juros_conta_gold(self):
        self.factory.realizar_emprestimo(self.conta_gold, 500, 5)
        self.assertEqual(
            self.factory.aplicar_juros_conta_gold(self.conta_gold),
            "Juros aplicados. Novo saldo do empréstimo: 510.0",
        )


if __name__ == "__main__":
    unittest.main()
