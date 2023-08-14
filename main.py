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

    args = parser.parse_args()
    nomes = args.nomes
    localidades = args.localidades
    sexo = args.sexo

    if not nomes:
        return print(Ranking().geral(localidades, sexo))

    if localidades:
        return print(
            Ranking(
                nomes_frequencia_localidade=Item(nomes, sexo).frequencia_localidades(
                    localidades
                )
            ).nomes(sexo)
        )

    return print(Ranking(Item(nomes, sexo).frequencia_nome()).nomes(sexo))


if __name__ == "__main__":
    main()
