from contas.gold import ContaGold
from contas.silver import ContaSilver


class FactoryContas:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, titular: str, saldo_inicial: float):
        titular = titular.upper()
        numero_conta = len(self.contas) + 1

        if saldo_inicial < 5000:
            conta = ContaSilver(titular, numero_conta, saldo_inicial)
        else:
            conta = ContaGold(titular, numero_conta, saldo_inicial)

        self.contas[titular] = conta
        return f"Conta {('Silver', 'Gold')[saldo_inicial >= 5000]} criada com sucesso. Titular: {titular} Número da conta: {numero_conta}"

    def obter_conta(self, titular: str):
        return self.contas.get(titular.upper())

    def depositar_em_conta(self, conta, valor):
        return conta.depositar(valor)

    def sacar_da_conta(self, conta, valor):
        return conta.sacar(valor)

    def realizar_emprestimo(self, conta, valor, tempo):
        if conta.tipo == "Gold":
            return conta.conceder_emprestimo(valor, tempo)
        return "Empréstimo não disponível para este tipo de conta."

    def aplicar_juros_conta_gold(self, conta):
        if isinstance(conta, ContaGold):
            return conta.aplicar_juros()
        return "Juros aplicáveis somente para contas Gold."
