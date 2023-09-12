from argparse import ArgumentParser
from itens.item import Item
from rankings.ranking import Ranking
from services.ibge import Ibge


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

    return parser


def definicao_titulo(is_nome: bool, is_localidade: bool, sexo="") -> str:
    titulo = "Ranking geral dos nomes"

    if is_nome:
        titulo = "Ranking dos nomes"

    if sexo == "M":
        titulo += " do sexo Masculino"

    if sexo == "F":
        titulo += " do sexo Feminino"

    if is_localidade:
        titulo += f" por localidade"

    return f"{titulo}:\n"


def busca_ranking(nomes=[], sexo="", localidade="") -> str:
    ibge = Ibge(sexo)
    ranking = Ranking()

    if nomes:
        itens = []

        for nome in nomes:
            item = Item(nome, ibge.busca_frequencia(nome, localidade))
            itens.append(item)

        return ranking.gera_ranking_nomes(itens)

    return ranking.gera_ranking_geral(ibge.busca_ranking_geral(localidade))


def main():
    args = arguments().parse_args()
    nomes = args.nomes
    localidades = args.localidades
    sexo = args.sexo
    is_nome = not nomes == None
    is_localidade = not localidades == None
    titulo = definicao_titulo(is_nome, is_localidade, sexo)

    conteudo = titulo

    if localidades:
        for localidade in localidades:
            conteudo += f"\nLocalidade: {localidade}\n"
            conteudo += f"{busca_ranking(nomes,sexo,localidade)}\n"
    else:
        conteudo += busca_ranking(nomes, sexo)

    print(conteudo)


if __name__ == "__main__":
    main()
