from itens import Item
from rankings import Ranking
from scripts import arguments


def main():
    args = arguments().parse_args()
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
