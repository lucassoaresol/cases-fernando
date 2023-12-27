from datetime import datetime


class Conta:
    saldo = 0
    extrato = []

    def obter_data_atual(self):
        data_atual = datetime.now()
        formato_personalizado = "%d-%m-%Y  %H:%M:%S"
        data_formatada = data_atual.strftime(formato_personalizado)

        return data_formatada

    def obter_extrato(self):
        extrato = "Extrato da conta:\n\n"

        for transacao in self.extrato:
            extrato += f"{transacao}\n"

        extrato += f"\nSaldo Atual: {self.saldo:.2f}"

        return extrato

    def efetuar_saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"{self.obter_data_atual()}  Saque        -{valor:.2f}")
            return f"Saque de {valor:.2f} realizado com sucesso. Novo saldo: {self.saldo:.2f}."

        elif valor <= 0:
            return "O valor de saque deve ser maior que zero."

        else:
            return "Saldo insuficiente para realizar o saque."

    def efetuar_deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"{self.obter_data_atual()}  Depósito     +{valor:.2f}")
            return f"Depósito de {valor:.2f} realizado com sucesso. Novo saldo: {self.saldo:.2f}."

        else:
            return "O valor de depósito deve ser maior que zero."


class ContaSilver(Conta):
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def solicitar_emprestimo(self, montante_emprestimo, prazo_pagamento_meses):
        return "Empréstimo bloqueado para contas Silver."

    def calcular_e_aplicar_juros(self):
        return "Esta funcionalidade não está disponível para contas Silver."


class ContaGold(Conta):
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.valor_emprestimo_atual = 0
        self.taxa_juros_mensal = 0.03

    def solicitar_emprestimo(self, montante_emprestimo, prazo_pagamento_meses):
        self.saldo += montante_emprestimo
        self.extrato.append(
            f"{self.obter_data_atual()}  Empréstimo   +{montante_emprestimo:.2f}"
        )
        self.valor_emprestimo_atual += montante_emprestimo
        return f"Empréstimo aprovado! Você recebeu {montante_emprestimo:.2f}. O pagamento deve ser feito em {prazo_pagamento_meses} meses. Novo saldo: {self.saldo:.2f}."

    def calcular_e_aplicar_juros(self):
        if self.valor_emprestimo_atual > 0:
            self.valor_emprestimo_atual *= 1 + self.taxa_juros_mensal
            return f"Juros aplicados com sucesso. O saldo do empréstimo atualizado é: {self.valor_emprestimo_atual:.2f}."

        else:
            return "Não há empréstimo pendente. Nenhum juro foi aplicado."


class FactoryContas:
    @staticmethod
    def criar_conta(tipo):
        if tipo.lower() == "silver":
            return ContaSilver()
        elif tipo.lower() == "gold":
            return ContaGold()
        else:
            raise ValueError("Tipo de conta inválido")
