from argparse import ArgumentParser
from itens import Item
from rankings import Ranking
from services import Ibge


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
    title = "Ranking dos nomes:"

    if nomes:
        nomes_frequencia = []

        for nome in nomes:
            item = Item(nome, Ibge().busca_frequencia(nome))
            nomes_frequencia.append({"nome": item.nome, "frequencia": item.frequencia})

        dados = Ranking().orderna_nomes(nomes_frequencia)

    else:
        title = "Ranking geral dos nomes:"
        dados = Ibge().busca_ranking_geral()

    return print(f"{title}\n{Ranking().gera_ranking(dados)}")


if __name__ == "__main__":
    main()
