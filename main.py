import argparse
from itens import Item
from rankings import Ranking


def main():
    parser = argparse.ArgumentParser(
        description="Obter um ranking de nomes brasileiros baseado na frequência dos mesmos através do último senso IBGE disponível"
    )

    parser.add_argument(
        "-n",
        "--nomes",
        nargs="+",
        type=str,
        help="Digite os nomes que deseja obter o ranking",
    )

    args = parser.parse_args()
    nomes = args.nomes

    nomes_frequencia = []

    if not nomes:
        return print(f"Ranking geral dos nomes:\n{Ranking().geral()}")

    for nome in nomes:
        nomes_frequencia.append(Item(nome).get_frequencia())

    return print(f"Ranking dos nomes:\n{Ranking(nomes_frequencia).nomes()}")


if __name__ == "__main__":
    main()
