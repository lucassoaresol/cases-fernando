from argparse import ArgumentParser
from services.ibge import Ibge


def type_localidade(localidade: str):
    resposta = Ibge().busca_localidade(localidade)

    if resposta:
        return resposta["id"]
    else:
        raise ValueError


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
        type=type_localidade,
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
