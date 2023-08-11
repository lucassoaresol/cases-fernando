from itens import Item
from rankings import Ranking


def main():
    nomes_frequencia = []
    nomes = input(
        "Digite uma lista de nomes separados por ',' para obter o ranking ou deixe em branco para obter o ranking geral: "
    )

    if len(nomes.strip()) == 0:
        return print(Ranking().geral())

    for nome_input in nomes.split(","):
        nome = nome_input.strip().upper()
        if len(nome):
            try:
                nomes_frequencia.append(Item(nome).get_frequencia())
            except IndexError:
                return print(f"{nome} é inválido, tente novamente!")

    return print(Ranking(nomes_frequencia).nomes())


if __name__ == "__main__":
    main()
