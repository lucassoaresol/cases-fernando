from itens import Item
from rankings import Ranking
from scripts import arguments


def main():
    args = arguments().parse_args()
    nomes = args.nomes
    localidades = args.localidades
    sexo = args.sexo
    is_localidade = not localidades == None
    ranking = Ranking(is_localidade, sexo)

    if not nomes:
        return print(ranking.geral(localidades))

    nomes_frequencia = Item(nomes, sexo).frequencia(localidades)

    return print(ranking.nomes(nomes_frequencia))


if __name__ == "__main__":
    main()
