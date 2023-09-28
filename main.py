from argparse import ArgumentParser
from rankings.ranking import Ranking
from services.ibge import Ibge
from urllib3.exceptions import MaxRetryError


def arguments() -> ArgumentParser:
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

    parser.add_argument(
        "-l",
        "--localidades",
        nargs="+",
        type=int,
        help="Digite as localidades que deseja obter o ranking",
    )

    parser.add_argument(
        "-s",
        "--sexo",
        type=str,
        choices=["M", "F"],
        help="Digite 'M', para o sexo masculino, ou 'F', para o feminino caso deseje obter o ranking por sexo",
    )

    parser.add_argument(
        "-r",
        "--retry",
        type=int,
        default=3,
        help="Definir o número de tentativas",
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=5,
        help="Definir o timeout",
    )

    return parser


def main():
    args = arguments().parse_args()
    nomes = args.nomes
    localidades = args.localidades
    sexo = args.sexo
    retry = args.retry
    timeout = args.timeout
    ibge = Ibge(retry, timeout)

    try:
        print(Ranking(ibge, nomes, localidades, sexo).exibir_ranking())
    except MaxRetryError:
        return print("Número de tentativas excedido")


if __name__ == "__main__":
    main()
