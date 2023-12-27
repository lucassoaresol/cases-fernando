from contas import FactoryContas
import unittest


class TestConta(unittest.TestCase):
    def setUp(self):
        self.factory_contas = FactoryContas()

    def teste_criar_conta_raise(self):
        with self.assertRaises(ValueError) as context:
            self.factory_contas.criar_conta("")

        self.assertEqual(str(context.exception), "Tipo de conta inválido")

    def teste_obter_extrato(self):
        conta = self.factory_contas.criar_conta("gold")
        conta.efetuar_deposito(100)
        conta.solicitar_emprestimo(1000, 2)
        conta.efetuar_saque(100)
        conta.obter_extrato()

        self.assertEqual(
            len(conta.extrato),
            3,
        )

    def teste_obter_extrato_return(self):
        conta = self.factory_contas.criar_conta("silver")

        self.assertEqual(
            conta.obter_extrato(),
            f"Extrato da conta:\n\n\nSaldo Atual: {conta.saldo:.2f}",
        )

    def teste_efetuar_saque_negativo(self):
        conta = self.factory_contas.criar_conta("silver")

        self.assertEqual(
            conta.efetuar_saque(-1), "O valor de saque deve ser maior que zero."
        )

    def teste_efetuar_saque_saldo_insuficiente(self):
        conta = self.factory_contas.criar_conta("silver")

        self.assertEqual(
            conta.efetuar_saque(10), "Saldo insuficiente para realizar o saque."
        )

    def teste_efetuar_deposito_negativo(self):
        conta = self.factory_contas.criar_conta("gold")

        self.assertEqual(
            conta.efetuar_deposito(-1), "O valor de depósito deve ser maior que zero."
        )

    def teste_solicitar_emprestimo_silver(self):
        conta = self.factory_contas.criar_conta("silver")

        self.assertEqual(
            conta.solicitar_emprestimo(1000, 2),
            "Empréstimo bloqueado para contas Silver.",
        )

    def teste_calcular_e_aplicar_juros(self):
        conta = self.factory_contas.criar_conta("gold")
        conta.solicitar_emprestimo(1000, 2)

        self.assertEqual(
            conta.calcular_e_aplicar_juros(),
            f"Juros aplicados com sucesso. O saldo do empréstimo atualizado é: {conta.valor_emprestimo_atual:.2f}.",
        )

    def teste_calcular_e_aplicar_juros_err(self):
        conta = self.factory_contas.criar_conta("gold")

        self.assertEqual(
            conta.calcular_e_aplicar_juros(),
            "Não há empréstimo pendente. Nenhum juro foi aplicado.",
        )

    def teste_calcular_e_aplicar_juros_silver(self):
        conta = self.factory_contas.criar_conta("silver")

        self.assertEqual(
            conta.calcular_e_aplicar_juros(),
            "Esta funcionalidade não está disponível para contas Silver.",
        )


if __name__ == "__main__":
    unittest.main()
