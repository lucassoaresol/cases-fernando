from argparse import ArgumentParser
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

    return print(Ranking().gera_ranking(nomes))


if __name__ == "__main__":
    main()
