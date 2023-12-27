from contas import FactoryContas
import os


def exibir_menu():
    print("1. Criar conta Silver")
    print("2. Criar conta Gold")
    print("3. Extrato")
    print("4. Saque")
    print("5. Depósito")
    print("6. Empréstimo")
    print("7. Aplicar juros")
    print("8. Sair")


def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    factory_contas = FactoryContas()
    conta = None

    while True:
        exibir_menu()
        escolha = int(input("\nEscolha uma opção: "))

        limpar_terminal()

        if escolha == 1:
            conta = factory_contas.criar_conta("silver")
            print("Conta Silver criada com sucesso!")

        elif escolha == 2:
            conta = factory_contas.criar_conta("gold")
            print("Conta Gold criada com sucesso!")

        elif 3 <= escolha <= 7:
            if conta:
                if escolha == 3:
                    print(conta.obter_extrato())

                if escolha == 4:
                    valor = float(input("Valor do saque: "))
                    print(conta.efetuar_saque(valor))

                elif escolha == 5:
                    valor = float(input("Valor do depósito: "))
                    print(conta.efetuar_deposito(valor))

                elif escolha == 6:
                    montante_emprestimo = float(input("Valor do empréstimo: "))
                    prazo_pagamento_meses = int(
                        input("Digite a quantidade de meses para pagamento: ")
                    )
                    print(
                        conta.solicitar_emprestimo(
                            montante_emprestimo, prazo_pagamento_meses
                        )
                    )

                elif escolha == 7:
                    print(conta.calcular_e_aplicar_juros())

            else:
                print(
                    "Operação não permitida. Por favor, crie uma conta antes de prosseguir."
                )

        elif escolha == 8:
            print("Saindo do terminal bancário. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

        print("\n")


if __name__ == "__main__":
    main()
