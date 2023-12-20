from contas.conta import Conta
import unittest


class TestConta(unittest.TestCase):
    def setUp(self):
        self.conta = Conta("Titular", 12345, 1000)

    def teste_depositar_valido(self):
        self.assertEqual(self.conta.depositar(500), "Depósito realizado com sucesso.")
        self.assertEqual(self.conta.saldo, 1500)

    def teste_depositar_invalido(self):
        self.assertEqual(self.conta.depositar(-100), "Valor de depósito inválido.")

    def teste_sacar_valido(self):
        self.assertEqual(self.conta.sacar(200), "Saque realizado com sucesso.")
        self.assertEqual(self.conta.saldo, 800)

    def teste_sacar_invalido(self):
        self.assertEqual(
            self.conta.sacar(2000), "Valor de saque inválido ou saldo insuficiente."
        )

    def teste_mostrar_saldo(self):
        self.assertEqual(self.conta.mostrar_saldo(), "Saldo atual: 1000.00")


if __name__ == "__main__":
    unittest.main()
