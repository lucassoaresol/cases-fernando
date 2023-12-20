from contas.conta import Conta


class ContaGold(Conta):
    def __init__(self, titular: str, numero: int, saldo: float, taxa_juros=0.02):
        super().__init__(titular, numero, saldo, tipo="Gold")
        self.valor_emprestimo = 0
        self.taxa_juros = taxa_juros

    def conceder_emprestimo(self, valor: float, tempo: int):
        self.valor_emprestimo += valor
        return f"Empréstimo de {valor} concedido, a ser pago em {tempo} meses."

    def aplicar_juros(self):
        if self.valor_emprestimo > 0:
            self.valor_emprestimo *= 1 + self.taxa_juros
            return f"Juros aplicados. Novo saldo do empréstimo: {self.valor_emprestimo}"
        else:
            return "Não há empréstimo para aplicar juros."
