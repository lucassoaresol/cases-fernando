from argparse import ArgumentParser
from rankings.ranking import Ranking
from services.ibge import Ibge
from urllib3.exceptions import MaxRetryError


def type_decada(decada: str) -> int:
    result = int(decada)

    if result < 1930 or result > 2010 or result % 10 != 0:
        raise ValueError

    return result


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

    parser.add_argument(
        "-d",
        "--decadas",
        nargs="+",
        type=type_decada,
        help="Digite as décadas que deseja obter o ranking",
    )

    return parser


def main():
    args = arguments().parse_args()
    nomes = args.nomes
    localidades = args.localidades
    sexo = args.sexo
    retry = args.retry
    timeout = args.timeout
    decadas = args.decadas

    ranking = Ranking(Ibge(retry, timeout))

    ranking.define_titulo(nomes, sexo, localidades, decadas)
    ranking.gera_ranking(nomes, sexo, localidades, decadas)
    ranking.mostra_ranking()


if __name__ == "__main__":
    main()
