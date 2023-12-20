from contas.factory import FactoryContas


def exibir_menu():
    print("\n----- Menu do Banco -----")
    print("1: Criar conta")
    print("2: Acessar conta")
    print("3: Realizar Saque")
    print("4: Realizar Depósito")
    print("5: Realizar Empréstimo")
    print("6: Próximo mês")
    print("0: Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao


def main():
    contas = FactoryContas()
    while True:
        opcao = exibir_menu()

        if opcao == 1:
            titular = input("Nome do titular: ")
            conta = contas.obter_conta(titular)
            if not conta:
                valor = input("Saldo inicial: ")
                saldo_inicial = float(0 if valor == "" else valor)
                print(contas.criar_conta(titular, saldo_inicial))
            else:
                print("Já existe uma conta aberta para esse titular.")

        elif opcao == 2:
            titular = input("Nome do titular para acessar a conta: ")
            conta = contas.obter_conta(titular)
            if conta:
                print(conta.mostrar_saldo())
            else:
                print("Conta não encontrada.")

        elif opcao == 3:
            titular = input("Nome do titular para saque: ")
            conta = contas.obter_conta(titular)
            if conta:
                valor = float(input("Valor do saque: "))
                print(contas.sacar_da_conta(conta, valor))
            else:
                print("Conta não encontrada.")

        elif opcao == 4:
            titular = input("Nome do titular para depósito: ")
            conta = contas.obter_conta(titular)
            if conta:
                valor = float(input("Valor do depósito: "))
                print(contas.depositar_em_conta(conta, valor))
            else:
                print("Conta não encontrada.")

        elif opcao == 5:
            titular = input("Nome do titular para empréstimo: ")
            conta = contas.obter_conta(titular)
            if conta:
                valor = float(input("Valor do empréstimo: "))
                tempo = int(input("Tempo para pagamento (em meses): "))
                print(contas.realizar_emprestimo(conta, valor, tempo))
            else:
                print("Conta não encontrada.")

        elif opcao == 6:
            titular = input("Nome do titular para aplicar juros: ")
            conta = contas.obter_conta(titular)
            if conta:
                print(contas.aplicar_juros_conta_gold(conta))
            else:
                print("Conta não encontrada.")

        elif opcao == 0:
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
