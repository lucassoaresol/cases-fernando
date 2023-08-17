from argparse import ArgumentParser
from itens import Item
from rankings import Ranking


def main():
    parser = ArgumentParser(
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

    if not nomes:
        return print(f"Ranking geral dos nomes:\n{Ranking().geral()}")

    nomes_frequencia = Item(nomes).frequencia()

    return print(f"Ranking dos nomes:\n{Ranking().nomes(nomes_frequencia)}")


if __name__ == "__main__":
    main()
