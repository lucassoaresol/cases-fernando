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
        return print(Ranking().geral())

    for nome in nomes:
        nome = nome.upper()

        try:
            nomes_frequencia.append(Item(nome).get_frequencia())
        except IndexError:
            return print(f"o nome {nome} é inválido, tente novamente!")

    return print(Ranking(nomes_frequencia).nomes())


if __name__ == "__main__":
    main()
