from contas.conta import Conta


class ContaSilver(Conta):
    def __init__(self, titular: str, numero: int, saldo=0):
        super().__init__(titular, numero, saldo, tipo="Silver")

    def conceder_emprestimo(self, valor, tempo):
        return "Empréstimo não disponível para Conta Básica."
