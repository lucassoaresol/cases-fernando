from argparse import ArgumentParser


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
        help="Definir o número de tentativas",
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        help="Definir o timeout",
    )

    return parser
