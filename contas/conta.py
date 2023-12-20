class Conta:
    def __init__(self, titular: str, numero: int, saldo: float, tipo=None):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.tipo = tipo

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            return "Depósito realizado com sucesso."
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor: float):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return "Saque realizado com sucesso."
        else:
            return "Valor de saque inválido ou saldo insuficiente."

    def mostrar_saldo(self):
        return f"Saldo atual: {self.saldo:.2f}"
